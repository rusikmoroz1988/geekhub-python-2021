import sqlite3

class NoBanknotesError(Exception):
    def __init__(self, text):
        self.txt = text

def create_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INT,
        username TEXT,
        password TEXT,
        is_incasator INT);
        """)
  
    cursor.execute("""CREATE TABLE IF NOT EXISTS balances(
        userid INT,
        balance REAL);
        """) 
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS banknotes(
        banknote INT,
        count INT);
        """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
        userid INT,
        date_trans TEXT,
        event TEXT);
        """)     
    
    users = [ 
        {"username": "user1", "password": "user1", "is_incasator": 0},
        {"username": "user2", "password": "user2", "is_incasator": 0},
        {"username": "admin", "password": "admin", "is_incasator": 1}
        ]
    
    step = 1
    for item in users: 
        username = item["username"]
        password = item["password"]
        is_incasator = item["is_incasator"]
        
        if user_exist_in_base(username, password, connection) == -1:
            sql = "INSERT INTO users VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (step, username, password, is_incasator))       
        step += 1
        
    connection.commit()     
    connection.close()

def get_connection():
    return sqlite3.connect('atm.db')
      
def user_exist_in_base(username, password, connection = None, is_сollector = False):
    if connection == None:  
        connection = get_connection()
        
    cursor = connection.cursor()
    if is_сollector:
        cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND is_incasator=1", (username, password))
    else:    
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))       
    
    user_id = -1
    try:
        user_id   = cursor.fetchone()[0]
    except:
        pass
    return user_id

def add_user_to_base(username, password, is_сollector):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(userid) FROM users")
    
    try:
        max_id   = cursor.fetchone()[0] + 1
    except:
        max_id = 1
    
    sql = "INSERT INTO users VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (max_id, username, password, is_сollector))
    connection.commit()
    connection.close()
    
def create_transaction(ID, date, event):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO transactions VALUES (?, ?, ?)"
    cursor.execute(sql, (ID, date, event))
    connection.commit()
    connection.close()
    
def issued_banknotes(balance):
    connection = get_connection()
    cursor = connection.cursor()
    list_counts = []
    cursor.execute("SELECT * FROM banknotes")
    result = cursor.fetchall()
    my_list = []
    try:
        for item in result:
            my_list.append({"banknote": item[0], "count": item[1]})    
    except:
        return my_list
    
    my_list = sorted(my_list, key=lambda k: k['banknote'], reverse=True)
    
    list_counts = []
    last = 0
    if len(my_list) > 0:
        while balance > 0:    
            for item in my_list:
                count = item['count']
                banknote = item['banknote']
                if count == 0 or banknote == last:
                    continue
                cel = balance//banknote
                if cel == 0:
                    continue
                else:
                    if cel > count:
                        balance -= count * banknote
                        while count > 0:
                            list_counts.append(banknote)
                            count-=1                                    
                    else:
                        balance -= cel * banknote
                        while cel > 0:
                            list_counts.append(banknote) 
                            cel-=1
         
            if balance>0 and len(list_counts)!=0:
                last = list_counts.pop()
                balance = last + balance
                
    return list_counts
         
def delete_counts_from_banknote(list_counts, connection):
    if len(list_counts)!=0:
        print("Banknotes issued:\n")
        dict_in = dict((x, list_counts.count(x)) for x in set(list_counts)) 
        for key, value in dict_in.items():
            print('banknote: ', key, ' count: ', value)
    
    cursor = connection.cursor()
    for key,value in dict_in.items():
        cursor.execute("SELECT count FROM banknotes WHERE banknote=?", (int(key), ))
        try:
            count   = cursor.fetchone()[0]
            sql_update_query = """Update banknotes set count = ? where banknote = ?"""
            cursor.execute(sql_update_query, (count - int(value), int(key)))
        except:
            continue
        
def change_balance(ID, summa, operation):
    if summa%10!=0:
        return False
    original_summa = summa
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM balances WHERE userid=?", (ID, )) 
    if operation=='3':
        list_counts = issued_banknotes(original_summa)
        if len(list_counts)!=0:
            delete_counts_from_banknote(list_counts, connection)
        else:
            print("Not enough bills!")
            connection.commit()
            connection.close() 
            return False
        summa =- summa
       
    try:
        balance   = cursor.fetchone()[0]
        if operation=='3' and balance < original_summa:
            return False
        
        sql_update_query = """Update balances set balance = ? where userid = ?"""
        cursor.execute(sql_update_query, (balance + summa, ID))
    except:
        if summa<=0:
            return False
        sql_update_query = """INSERT INTO balances VALUES (?, ?)"""
        cursor.execute(sql_update_query, (ID, summa)) 
    
    connection.commit()
    connection.close()
    return True

def get_balance(ID):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM balances WHERE userid=?", (ID, ))
    try:
        return cursor.fetchone()[0]
    except:
        return 0

def show_banknotes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM banknotes")
    result = cursor.fetchall()
    if len(result)==0:
        print('No banknotes!')
    else:
        for item in result:
            print(f'banknote: {item[0]} count: {item[1]}\n', end='') 
   

def change_banknotes(list_banknot):
    connection = get_connection()
    cursor = connection.cursor()
    
    for item in list_banknot:
       cursor.execute("SELECT count FROM banknotes WHERE banknote=?", (item['banknote'], ))
       try:
           count = cursor.fetchone()[0]
           total = count + int(item['count'])
           if total < 0:
               raise NoBanknotesError("Not enough banknote ", item['banknote'])
           
           sql_update_query = """Update banknotes set count = ? where banknote = ?"""
           cursor.execute(sql_update_query, (total, int(item['banknote'])))
       except NoBanknotesError as nbe:
           print(nbe)
       except:
           sql_update_query = """INSERT INTO banknotes VALUES (?, ?)"""
           cursor.execute(sql_update_query, (int(item['banknote']), int(item['count'])))
    
    sql = 'DELETE FROM banknotes WHERE count=0'
    cursor.execute(sql)
    connection.commit()          
    connection.close()       
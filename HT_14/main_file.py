import sqlite3
import datetime
import requests

class NoBanknotesError(Exception):
    def __init__(self, text):
        self.txt = text

class PrivatBank(object):
    
    def __init__(self):
        self.url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'  
    
    def get_courses(self):
        response = requests.get(self.url)
        dict_json = response.json()
        return dict_json         

class Transaction(object):
    
    def __init__(self, dm, id_user, date, event):
        self.dm = dm
        self.id_user = id_user
        self.date = date
        self.event = event
    
    def create_transaction(self):
        self.dm.create_transaction(self.id_user, self.date, self.event)    

class Person(object):
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def authorization_success(self, dm):
        return dm.user_exist_in_base(self.login, self.password)    
    
    
    def create_user_(self, collector, id, dm):
        if collector:
            return Incassator(dm)
        else:
            return User(id, dm)
        


class Banknotes(object):
    
    def __init__(self, cursor):
        self.cursor = cursor
    
    def issued_banknotes(self, balance):
        list_counts = []
        cursor = self.cursor
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
    
    def delete_counts_from_banknote(self, list_counts):
        cursor = self.cursor
        if len(list_counts)!=0:
            print("Banknotes issued:\n")
            dict_in = dict((x, list_counts.count(x)) for x in set(list_counts)) 
            for key, value in dict_in.items():
                print('banknote: ', key, ' count: ', value)
    
        for key,value in dict_in.items():
            cursor.execute("SELECT count FROM banknotes WHERE banknote=?", (int(key), ))
            try:
                count   = cursor.fetchone()[0]
                sql_update_query = """Update banknotes set count = ? where banknote = ?"""
                cursor.execute(sql_update_query, (count - int(value), int(key)))
            except:
                continue
    
    def show_banknotes(self):
        cursor = self.cursor
        cursor.execute("SELECT * FROM banknotes")
        result = cursor.fetchall()
        if len(result)==0:
            print('No banknotes!')
        else:
            for item in result:
                print(f'banknote: {item[0]} count: {item[1]}\n', end='') 
    
    def change_banknotes(self, list_banknot):
        cursor = self.cursor
    
        for item in list_banknot:
            cursor.execute("SELECT count FROM banknotes WHERE banknote=?", (item['banknote'], ))
            try:
                count = cursor.fetchone()[0]
                total = count + int(item['count'])
                if total < 0:
                    raise NoBanknotesError("Not enough banknote " + item['banknote'])
           
                sql_update_query = """Update banknotes set count = ? where banknote = ?"""
                cursor.execute(sql_update_query, (total, int(item['banknote'])))
            except NoBanknotesError as nbe:
                print(nbe)
            except:
                sql_update_query = """INSERT INTO banknotes VALUES (?, ?)"""
                cursor.execute(sql_update_query, (int(item['banknote']), int(item['count'])))
    
        sql = 'DELETE FROM banknotes WHERE count=0'
        cursor.execute(sql)
  
    
class User(Person):
    
    def __init__(self, id, dm):
        self.id = id
        self.str_menu = ('Enter 1 for see the balance\n'
                        'Enter 2 for replenish the balance\n'
                        'Enter 3 for withdrawal of funds\n'
                        'Enter 4 to exit : ')
        self.dm = dm
    
    def actions_of_user(self):
         display_bool = True
         while display_bool:
             choice_menu = input(self.str_menu)
             if choice_menu == '1':
                 print(self.dm.get_balance(self.id))
             elif choice_menu == '2' or choice_menu == '3':
                 summ = eval(input("Enter money amount: "))
                 if summ <= 0:
                     print("Incorrect amount entered!")
                     continue        
                 if not (self.dm.change_balance(self.id, summ, choice_menu)):
                     print("Operation failed!")
                     continue
             
                 if choice_menu == '2':
                     Transaction(self.dm, self.id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'Balance complete at ' + str(summ)).create_transaction()
                 else: 
                     Transaction(self.dm, self.id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'Balance removed at ' + str(summ)).create_transaction()
             else:
                display_bool = False 
    
    

class Incassator(Person):
    
    def __init__(self, dm):
        self.str_choice_coll = ('Enter 1 for look at the obvious banknote\n'
                'Enter 2 change the number of bills\n'
                'Enter 3 to exit : ')   
        self.dm = dm
        self.banknote = Banknotes(self.dm.get_cursor())
    
    def actions_of_user(self):
        while True:
            choice = input(self.str_choice_coll)
            if choice == '1':
                self.banknote.show_banknotes()
            elif choice == '2':  
              list_dict  = []
              while True:
                denomination = input('Specify the denomination of the banknote (10, 20, 50, 100, 200, 500, 1000). Enter 0 to exit: ')
                if denomination=='0':
                    break
                count_dem = input('Enter the number of banknotes: ')
                list_dict.append({"banknote": denomination, "count": count_dem})
              self.banknote.change_banknotes(list_dict)
            elif choice == '3':
              break
        
    
class DatabaseManagement(object):
    
    def __init__(self):
        self.connection = sqlite3.connect('atm.db')
        self.cursor = self.connection.cursor()
        
    def get_cursor(self):
        return self.cursor
    
    def commit_changes(self):
        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()
    
    def create_transaction(self, id_user, date, event):
         sql = "INSERT INTO transactions VALUES (?, ?, ?)"
         self.cursor.execute(sql, (id_user, date, event))
    
    def user_exist_in_base(self, username, password, is_сollector = False):
        if is_сollector:
            self.cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND is_incasator=1", (username, password))
        else:    
            self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))       
    
        user_id = -1
        try:
            user_id   = self.cursor.fetchone()[0]
        except:
            pass
        return user_id
    
    def create_tables(self):
        cursor = self.cursor
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
            
            if self.user_exist_in_base(username, password) == -1:
                sql = "INSERT INTO users VALUES (?, ?, ?, ?)"
                cursor.execute(sql, (step, username, password, is_incasator))       
            step += 1
            
    def add_user_to_base(self, username, password, is_сollector = False):
        self.cursor.execute("SELECT MAX(userid) FROM users")
    
        try:
            max_id   = self.cursor.fetchone()[0] + 1
        except:
            max_id = 1
    
        sql = "INSERT INTO users VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql, (max_id, username, password, is_сollector))
        
        sql_update_query = """INSERT INTO balances VALUES (?, ?)"""
        self.cursor.execute(sql_update_query, (max_id, 0)) 
    
    def show_banknotes(self):
        self.cursor.execute("SELECT * FROM banknotes")
        result = self.cursor.fetchall()
        if len(result)==0:
            print('No banknotes!')
        else:
            for item in result:
               print(f'banknote: {item[0]} count: {item[1]}\n', end='') 
    
    def get_balance(self, id):
        cursor = self.cursor
        cursor.execute("SELECT balance FROM balances WHERE userid=?", (id, ))
        try:
            return cursor.fetchone()[0]
        except:
            return 0
    
    def change_balance(self, id, summa, operation):
        if summa%10!=0:
            return False
        original_summa = summa
        cursor = self.cursor
        cursor.execute("SELECT balance FROM balances WHERE userid=?", (id, )) 
        try:
            balance   = cursor.fetchone()[0]
        except:
            balance = 0
        banknote = Banknotes(cursor)
        if operation=='3':
            if balance < original_summa:
                return False    
            list_counts = banknote.issued_banknotes(original_summa)
            if len(list_counts)!=0:
                banknote.delete_counts_from_banknote(list_counts)
            else:
                print("Not enough bills!")
                return False
            summa =- summa
       
        try:
         
            sql_update_query = """Update balances set balance = ? where userid = ?"""
            cursor.execute(sql_update_query, (balance + summa, id))
        except:
            if summa<=0:
                return False
            sql_update_query = """INSERT INTO balances VALUES (?, ?)"""
            cursor.execute(sql_update_query, (id, summa)) 
    
        return True

class Bankomate(object):
    
    def __init__(self):
        self.dm = DatabaseManagement()
        self.dm.create_tables()
        self.privat_bank = PrivatBank()  
        self.str_choice= ('Enter 1 for authorization\n'
                    'Enter 2 for registration\n'
                    'Enter 3 for current exchange rate\n'
                    'Enter 4 to exit : ')
    
    def actions_of_bankomate(self):
        
        while True:        
            choice = input(self.str_choice)
            if choice == '1' or choice == '2':
                is_collector = input('The user is the collector (1-yes, 0 - no): ')=='1'
                username = input('Enter username: ')
                password = input('Enter password: ')
                person = Person(username, password)
                id = person.authorization_success(self.dm)
                if (choice == '1') and (id == -1):
                     print('There is no user with such data.')
                     continue
                
                object_user = person.create_user_(is_collector, id, self.dm)
                Transaction(self.dm, id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "Login successfully completed!").create_transaction()
                if choice == '2':
                    if id!=-1:
                        print('A user with such data already exists!')
                        continue 
                    self.dm.add_user_to_base(username, password)
                    id = self.dm.user_exist_in_base(username, password)
                    Transaction(self.dm, id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'A new user has been created').create_transaction()
                    if not is_collector:
                        Transaction(self.dm, id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'User balance created').create_transaction()
                else:
                    is_collector = (self.dm.user_exist_in_base(username, password, True)!=-1)
            elif choice == '3':
                list_currancy = PrivatBank().get_courses()
                for item in list_currancy:
                    print(item['ccy'], ":", "buy:", item['buy'], "sale:", item['sale'])
                continue
            elif choice == '4':
                break
            else:
                print("There is no such option!")
                continue
            
            object_user.actions_of_user()
        self.dm.commit_changes()
        self.dm.close_connection()

Bankomate().actions_of_bankomate()


import datetime
import database_management as dbm
import requests

def do_request_PB():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    dict_json = response.json()
    return dict_json

def user(ID):
     display_bool = True
     while display_bool:
         str_menu = ('Enter 1 for see the balance\n'
                        'Enter 2 for replenish the balance\n'
                        'Enter 3 for withdrawal of funds\n'
                        'Enter 4 to exit : ')
         choice_menu = input(str_menu)
         if choice_menu == '1':
             print(dbm.get_balance(ID))
         elif choice_menu == '2' or choice_menu == '3':
             summ = eval(input("Enter money amount: "))
             if summ <= 0:
                 print("Incorrect amount entered!")
                 continue        
             if not (dbm.change_balance(ID, summ, choice_menu)):
                 print("Operation failed!")
                 continue
             if choice_menu == '2':
                  dbm.create_transaction(ID, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'Balance complete at ' + str(summ)) 
             else:
                  dbm.create_transaction(ID, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'Balance removed at ' + str(summ)) 
         else:
            display_bool = False 

def collector():
    while True:
        str_choice_coll= ('Enter 1 for look at the obvious banknote\n'
                'Enter 2 change the number of bills\n'
                'Enter 3 to exit : ')   
        
        choice = input(str_choice_coll)
        if choice == '1':
            dbm.show_banknotes()
        elif choice == '2':  
            list_dict  = []
            while True:
                denomination = input('Specify the denomination of the banknote (10, 20, 50, 100, 200, 500, 1000). Enter 0 to exit: ')
                if denomination=='0':
                    break
                count_dem = input('Enter the number of banknotes: ')
                list_dict.append({"banknote": denomination, "count": count_dem})
            dbm.change_banknotes(list_dict)
        elif choice == '3':
            break

def start():
    dbm.create_database()
    while True:
        str_choice= ('Enter 1 for authorization\n'
                'Enter 2 for registration\n'
                'Enter 3 for current exchange rate\n'
                'Enter 4 to exit : ')
        choice = input(str_choice)
        
        is_collektor = False
        if choice == '1' or choice == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')
            id_user = dbm.user_exist_in_base(username, password)
            if (choice == '1') and (id_user == -1):
                print('There is no user with such data.')
                continue
             
            dbm.create_transaction(id_user, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "Login successfully completed!")
            if choice == '2':
               if id_user!=-1:
                    print('A user with such data already exists!')
                    continue    
               is_collektor = input('The user is the collector (1-yes, 0 - no): ')=='1'
               dbm.add_user_to_base(username, password, is_collektor)
               id_user = dbm.user_exist_in_base(username, password) 
               dbm.create_transaction(id_user, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'A new user has been created') 
               if not is_collektor:
                   dbm.create_transaction(id_user, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'User balance created') 
            else:
                is_collektor = (dbm.user_exist_in_base(username, password, None, True)!=-1)
                
        elif choice == '3':
            list_currancy = do_request_PB()
            for item in list_currancy:
                print(item['ccy'], ":", "buy:", item['buy'], "sale:", item['sale'])
            continue
        elif choice == '4':
            break
        else:
            print("There is no such option!")
            continue  
        
        if is_collektor:
            collector()
        else:
            user(id_user)
    
1
start()
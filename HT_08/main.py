import user_management as um
import balance_management as bm 
import transaction_management as tm
import banknote_management as bkm
import datetime

def user(username):
     display_bool = True
     while display_bool:
         str_menu = ('Enter 1 for see the balance\n'
                        'Enter 2 for replenish the balance\n'
                        'Enter 3 for withdrawal of funds\n'
                        'Enter 4 to exit : ')
         choice_menu = input(str_menu)
         if choice_menu == '1':
             print(bm.get_balance(username))
         elif choice_menu == '2' or choice_menu == '3':
             summ = eval(input("Enter money amount: "))
             if summ <= 0:
                 print("Incorrect amount entered!")
                 continue        
             if not (bm.balance_change(username, summ, choice_menu)):
                 print("Operation failed!")
                 continue
             if choice_menu == '2':
                  tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Balance complete at ' + str(summ)}) 
             else:
                  tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Balance removed at ' + str(summ)}) 
         else:
            display_bool = False        


def collector():
    while True:
        str_choice_coll= ('Enter 1 for look at the obvious banknote\n'
                'Enter 2 change the number of bills\n'
                'Enter 3 to exit : ')   
        
        choice = input(str_choice_coll)
        if choice == '1':
            bkm.show_banknotes()
        elif choice == '2':  
            list_dict  = []
            while True:
                denomination = input('Specify the denomination of the banknote (10, 20, 50, 100, 200, 500, 1000). Enter 0 to exit: ')
                if denomination=='0':
                    break
                count_dem = input('Enter the number of banknotes: ')
                list_dict.append({"banknote": denomination, "count": count_dem})
            bkm.change_banknotes(list_dict)
        elif choice == '3':
            break
            
                
def start():
    while True:
        str_choice= ('Enter 1 for authorization\n'
                'Enter 2 for registration\n'
                'Enter 3 to exit : ')
        choice = input(str_choice)
        
        is_collektor = False
        if choice == '1' or choice == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')
            if (choice == '1') and not(um.user_exists(username, password)):
                print('There is no user with such data.')
                continue
             
            tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Login successfully completed'})
            if choice == '2':
                if um.user_exists(username, password):
                    print('A user with such data already exists!')
                    continue    
                is_collektor = input('The user is the collector (1-yes, 0 - no): ')=='1'
                um.add_new_user(username, password, is_collektor)
                tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'A new user has been created'}) 
                if not is_collektor:
                    bm.create_balance_file(username)
                    tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'User balance created'}) 
            else:
                is_collektor = um.user_is_collector(username, password)
        elif choice == '3':
            break
        else:
            print("There is no such option!")
            continue  
        
        if is_collektor:
            collector()
        else:
            user(username)
        
start()
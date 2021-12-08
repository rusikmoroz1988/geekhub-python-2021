import user_management as um
import balance_management as bm 
import transaction_management as tm
import datetime

def start():
    while True:
        str_choice= ('Enter 1 for authorization\n'
                'Enter 2 for registration\n'
                'Enter 3 to exit : ')
        choice = input(str_choice)
        
        if choice == '1' or choice == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')
            if (choice == '1') and not(um.user_exists(username, password)):
                print('There is no user with such data.')
                continue
                
            tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Login successfully completed'})
            if choice == '2':
                um.add_new_user(username, password)
                tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'A new user has been created'}) 
                bm.create_balance_file(username)
                tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'User balance created'}) 
        elif choice == '3':
            break
        else:
            print("There is no such option!")
            continue
        
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
                if not (bm.balance_change(username, summ, choice_menu)):
                    print("Operation failed!")
                    continue
                if choice_menu == '2':
                   tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Balance complete at ' + str(summ)}) 
                else:
                   tm.create_transaction(username, {'user': username, 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 'event': 'Balance removed at ' + str(summ)}) 
            else:
                display_bool = False
        
        if not display_bool:
            break

start()
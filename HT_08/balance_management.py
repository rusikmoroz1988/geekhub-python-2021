import banknote_management as bm
import csv

def create_balance_file(username):
    filename = username + "_balance.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("0")

def balance_change(username, summ, operation):
    filename = username + "_balance.txt"
    balance = 0
    with open(filename, 'r') as f:
        balance = eval(f.read())
    if operation=='3':
        if balance < summ:
            return False
        if summ%10!=0:
            return False    
        list_counts = bm.issued_banknotes(summ)
        if len(list_counts)!=0:
            delete_counts_from_banknote(list_counts)        
        balance -= summ
    else:
        balance += summ
    
    with open(filename, 'w',  encoding='utf-8') as f:
        f.write(str(balance))
    return True
        
def get_balance(username):
     filename = username + "_balance.txt"
     with open(filename, 'r') as f:
         return f.read()

def delete_counts_from_banknote(list_counts):
     with open("banknote.csv", encoding='utf-8') as r_file:
         file_reader = csv.DictReader(r_file, delimiter = ",")
         my_list = list(file_reader)
         if len(list_counts)!=0:
             print("Banknotes issued:\n")
             dict_in = dict((x, list_counts.count(x)) for x in set(list_counts)) 
             for key, value in dict_in.items():
                  print('banknote: ', key, ' count: ', value)
         
         for item in my_list:
             count = int(item['count'])
             item['count'] = str(count - list_counts.count(int(item['banknote']))) 
         
         bm.change_banknotes(list(filter(lambda my_list: my_list['count'] != '0', my_list)))
         
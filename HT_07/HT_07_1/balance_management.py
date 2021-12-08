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
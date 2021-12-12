import json
    
def create_transaction(username, transaction):
    filename = username + "_transactions.json"
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(transaction, f, indent=2)

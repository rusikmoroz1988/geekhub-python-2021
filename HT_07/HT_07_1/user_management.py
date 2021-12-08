import json

def user_exists(username, password):
    with open('users.json', 'r') as f:
        try:
            users = json.load(f)
        except:
            return False
        
        return next((item for item, x in enumerate(users) if x["username"] == username and x["password"] == password), None) != None

def add_new_user(username, password):
     with open('users.json', 'r+') as f:
         try:
             jsonObject = json.load(f)
             f.seek(0)
             jsonObject.append({"username": username, "password": password})
             json.dump(jsonObject, f)
         except:
             json.dump([{"username": username, "password": password}], f)
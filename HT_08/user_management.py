import json

def user_exists(username, password, is_сollector = False):
    with open('users.json', 'r') as f:
        try:
            users = json.load(f)
        except:
            return False
        if is_сollector:
            return next((item for item, x in enumerate(users) if x["username"] == username and x["password"] == password and x["inkk"] == is_сollector), None) != None
        else:
            return next((item for item, x in enumerate(users) if x["username"] == username and x["password"] == password), None) != None

def add_new_user(username, password, is_сollector = False):
     with open('users.json', 'r+') as f:
         try:
             jsonObject = json.load(f)
             f.seek(0)
             jsonObject.append({"username": username, "password": password, "inkk": is_сollector})
             json.dump(jsonObject, f)
         except:
             json.dump([{"username": username, "password": password, "inkk": is_сollector}], f)
     
def user_is_collector(username, password):
    return user_exists(username, password, True)

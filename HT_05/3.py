####################################Task:
# На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) 
# - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, 
# користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, 
# наприклад:
#     Name: vasya
#     Password: wasd
#     Status: password must have at least one digit
#     -----
#     Name: vasya
#     Password: vasyapupkin2000
#     Status: OK
# P.S. Не забудьте використати блок try/except ;)

class LoginException(Exception):
    pass

class LoginUnderscoreException(Exception):
    pass

class PasswordException(Exception):
    pass

class PasswordLenghtException(Exception):
    pass

def validation(name, password):
    length_name = len(name)
    length_password = len(password)
    is_digit = any(map(str.isdigit, password))
    status = 'OK'
    try:
        if length_name < 3 or length_name > 50:
            raise LoginException
        elif length_password < 8:
            raise PasswordLenghtException
        elif not is_digit:
            raise PasswordException  
        elif name.find("_")>-1:
            raise LoginUnderscoreException
    except LoginException:
        status = 'the name must be at least 3 characters and at most 50'
    except PasswordLenghtException:
        status = 'password must be at least 8 characters long' 
    except PasswordException:
        status = 'password must have at least one digit'
    except LoginUnderscoreException:
        status = 'forbidden character found in name'
    return status

list_of_users = [
     { "name": "John", "password": "1djfghdfjkghf"},
     { "name": "To", "password": "rewtrtt56" },
     { "name": "Mark", "password": "rue56"},
     { "name": "Peter", "password": "hdfoghjsihgj" },
     { "name": "John_", "password": "1djfghdfjkghf" }
    ]

step = 1
for item in list_of_users:
    print("Name: ", item['name'])
    print("Password: ", item['password'])
    print("Status: ", validation(item['name'], item['password']))
    if step != len(list_of_users): 
        print("-------------------")
    step+=1
    
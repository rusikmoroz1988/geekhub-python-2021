####################################Task:
# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

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

print(validation('John', '1djfghdfjkghf'))
print(validation('To', 'rewtrtt56'))
print(validation('John', 'rue56'))
print(validation('John', 'hdfoghjsihgj'))
print(validation('John_', '1djfghdfjkghf'))
    
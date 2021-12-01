####################################Task:
# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) 
# і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# - якщо введено коректну пару ім'я/пароль - вертається <True>;
# - якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
# інакше (<silent> == <False>) - породжується виключення LoginException

class LoginException(Exception):
    pass

def data_correct(username, password, silent = False):
    list_of_users = [
     { "username": "Tomas", "password": "111_dfgdffdgdfg"},
     { "username": "Markus", "password": "575467488" },
     { "username": "Pamella", "password": "333333077070"},
     { "username": "John", "password": "345335" },
     { "username": "James", "password": "11111111111" }
    ]

    size = len(list(filter(lambda item: item['username'] == username and item['password'] == password, list_of_users)))
    if size != 0:
        return True
    elif size == 0 and silent:
        return False
    else: 
        raise LoginException("Login or password entered incorrectly!") 
    
print(data_correct("Tomas", "111_dfgdffdgdfg"))
print(data_correct("Pamella", "111_dfgdf", True))
print(data_correct("Pamella", "111111"))     
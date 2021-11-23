####################################Task:
# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" 
# вiдповiдь повертали рiзницю чисел. 
# -  Повиннi опрацювати такi умови:
# - x > y;       вiдповiдь - х бiльше нiж у на z
# - x < y;       вiдповiдь - у бiльше нiж х на z
# - x == y.      вiдповiдь - х дорiвнює z

def equality_of_variables(x, y):
    result = ''
    z = 0
    if (x > y):
       z = x - y
       result = f'{x} more for {y} on {z}' 
    elif (x < y):
        z = y - x
        result = f'{y} more for {x} on {z}' 
    else:
        z = x
        result = f'{x} is equal to {z}' 
    return result

x_number = int(input('Enter the number x: '))
y_number = int(input('Enter the number y: '))
print(equality_of_variables(x_number, y_number))

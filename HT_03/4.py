####################################Task:
# Створiть 3 рiзних функцiї (на ваш вибiр). 
# Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, 
# яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
import math, random

def square_number(random_number):
   return random_number**2 

def number_cube(random_number):
    return random_number**3

def square_root(random_number):
    return math.sqrt(random_number)

def get_arithmetic_result(random_number):
    result = dict()
    result['Square'] = square_number(random_number)
    result['Cobe'] = number_cube(random_number)
    result['Square root'] = square_root(random_number)
    return result

random_number = random.randint(0, 10)
print('Entered a random number is: ', random_number)
arithmetic_result = get_arithmetic_result(random_number)
for key,value in arithmetic_result.items():
    print(key, ': ', value)
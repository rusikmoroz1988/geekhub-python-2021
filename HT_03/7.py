####################################Task:
# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи 
# - один з яких операцiя, яку зробити!

def calculate(number_1, number_2, operation):
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/' and number_2 != 0:
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Data entered incorrectly!')

data_list = input('Enter math operation you would like to complete (for example, 8 + 7): ').split(" ")
calculate(eval(data_list[0]), eval(data_list[2]), data_list[1])

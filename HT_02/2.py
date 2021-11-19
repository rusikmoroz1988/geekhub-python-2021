####################################Task:
# Написати скрипт, який пройдеться по списку, який складається із кортежів, 
# і замінить для кожного кортежа останнє значення.
# Список із кортежів можна захардкодити. Значення, 
# на яке замінюється останній елемент кортежа вводиться користувачем.
# Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). 
# Кількість елементів в кортежу повинна бути різна.

value = input('Input the value to which the last element of the tuple is replaced:')
list_of_tuples = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]

for index_of_list in range(len(list_of_tuples)):
    item = list_of_tuples[index_of_list]
    modified_tuple = item[:-1] + (value, )
    list_of_tuples[index_of_list] = modified_tuple

print(list_of_tuples)
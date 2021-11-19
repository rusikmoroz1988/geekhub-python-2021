####################################Task:
# Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, 
# з ключами від 0 до введеного числа,
# а значення для цих ключів - це квадрат ключа.

dictionary = {}
input_number = int(input("Please enter a positive integer: "))
for step in range(input_number + 1):
    dictionary[step] = step**2
print(dictionary)

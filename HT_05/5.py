####################################Task:
# Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), 
# сума цифр кожного елемент якого буде дорівнювати 10.
#   Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]

print([item for item in range(100) if sum([int(step) for step in str(item)])==10])
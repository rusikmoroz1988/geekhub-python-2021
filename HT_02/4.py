####################################Task:
# Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись.
# Дані можна "захардкодити".

dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
new_dict = dict(list(dict_1.items()) + list(dict_2.items()) + list(dict_3.items())) 
print(new_dict)
####################################Task:
# Написати скрипт, який залишить в словнику тільки пари 
# із унікальними значеннями (дублікати значень - видалити). Словник для роботи захардкодити свій.

basic_dict = {'a': 5, 'b': 10, 'c': 69, 'd': 10}
source_dict = dict()
list_of_values = []
for key, value in basic_dict.items():
   if not list_of_values.count(value):
        source_dict[key] = value
        list_of_values.append(value)
print(source_dict)
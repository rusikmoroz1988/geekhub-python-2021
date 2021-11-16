####################################Tasks:
# Write a script which accepts a sequence of comma-separated numbers 
# from user and generate a list and a tuple with those numbers.

sequ_of_numbers = input("Input sequence of numbers:")
list_of_numbers = sequ_of_numbers.split(',')
print("List : ", list_of_numbers)

tuple_of_numbers = tuple(list_of_numbers)
print("Tuple : ", tuple_of_numbers)
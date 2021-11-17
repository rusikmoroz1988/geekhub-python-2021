####################################Tasks:
#Write a script to check whether a specified value is contained in a group of values.

value = eval(input('Input value: '))
set_of_values = set(input('Input list of values: ').split(" "))
set_of_value = set()
set_of_value.add(str(value))
print(not set_of_values.isdisjoint(set_of_value))
####################################Tasks:
# Write a script to sum of the first n positive integers.

first_numbers = int(input("Enter the number of positive numbers:"))
list_numbers = [num for num in range(0,first_numbers)]
print(sum(list_numbers))

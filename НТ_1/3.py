####################################Tasks:
# Write a script to sum of the first n positive integers.

first_numbers = int(input("Enter the number of positive numbers:"))
summ = 0
for num in range(0, first_numbers):
    summ+=num
print(summ)

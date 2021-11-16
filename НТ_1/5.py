####################################Tasks:
# Write a script to convert decimal to hexadecimal

number_decimal = int(input("Input decimal number:"))
print(hex(number_decimal).split('x')[-1])
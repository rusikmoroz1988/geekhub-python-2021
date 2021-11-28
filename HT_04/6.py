####################################Task:
# Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, 
# збільшити його на 100, якщо дорівнює 0, не змінювати.

def arithmetic_func(digit):
    if digit > 0:
        digit = digit**2
    elif digit < 0:
        digit += 100
    print(digit) 
    
arithmetic_func(eval(input('Enter the number: ')))
        

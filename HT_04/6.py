####################################Task:
# Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, 
# збільшити його на 100, якщо дорівнює 0, не змінювати.

arithmetic_func = lambda x: x**2 if x>0 else (x+100 if x<0 else x)
print(arithmetic_func(eval(input('Enter the number: '))))
        

# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class NumberOfCopies(object):
    
    count = 0
    
    def __init__(self): 
        NumberOfCopies.count += 1   

first = NumberOfCopies()
second = NumberOfCopies()
print(NumberOfCopies.count)
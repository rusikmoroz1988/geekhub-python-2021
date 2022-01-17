# Створити клас Calc, який буде мати атребут last_result та 4 методи. 
# Методи повинні виконувати математичні операції з 2-ма числами, 
# а саме додавання, віднімання, множення, ділення.
#  - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#  - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#  - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

class Calc(object):
    """The class Calc is used to perform mathematical operations between two numbers

    
    The main purpose - to perform mathematical operations between two numbers

    
    Attributes
    ----------
    last_result : None or Float
        the result of a previous mathematical operation


    Methods
    -------
    add()
        adds 2 numbers
    subtraction()
        subtraction operation between two numbers
    multiplication()
        multiplication operation between two numbers
    division()
        division operation between two numbers
    
    """
    
    last_result  = None
    
    def add(self, a, b):
        self.last_result = a + b
    
    def subtraction(self, a, b):
        self.last_result = a - b
    
    def multiplication(self, a, b):
        self.last_result = a * b
    
    def division(self, a, b):
        try: 
            self.last_result = a / b      
        except ZeroDivisionError:
            print("Division not performed. The number b should not be equal to 0!")


while True:
    try:
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
    except ValueError:
        print('The number was entered incorrectly!')
        continue
         
    obj_calc = Calc()
    print(obj_calc.last_result) 
    obj_calc.add(a, b)
    print(obj_calc.last_result)
    obj_calc.subtraction(a, b)
    print(obj_calc.last_result)
    obj_calc.multiplication(a, b)
    print(obj_calc.last_result)
    obj_calc.division(a, b)
    print(obj_calc.last_result)
    break
    
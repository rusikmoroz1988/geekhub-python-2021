####################################Task:
# Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, 
# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

def get_perimeter(side):
    return side * 4   

def get_square(side):
    return side**2 

def get_diagonal(side):
    return  2**(0.5) * side

def square(side):
    return (get_perimeter(side), get_square(side), get_diagonal(side))

tuple_of_operations = square(eval(input("Enter the side of the square: ")))
print("Perimetr: %s\nSquare: %s\nDiagonal: %s" % tuple_of_operations)

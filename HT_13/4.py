# Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор 
# фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його 
# та додавали початкові розміри.

class Figure(object):
    
    def __init__(self, color):
        self.color = color
    

class Oval(Figure):
    
    def __init__(self, color, major_axis, minor_axis): 
        super().__init__(color)
        self.major_axis = major_axis   
        self.minor_axis = minor_axis

class Square(Figure):
    
    def __init__(self, color, side): 
        super().__init__(color)
        self.side = side   

new_figure = Figure('red')
print('Color of figure: ', new_figure.color)

new_oval = Oval('green', 2, 3)
print('Color of oval: ', new_oval.color)

new_square = Square('blue', 4)
print('Color of square: ', new_square.color)

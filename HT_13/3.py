# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням 
# white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) 
# містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

class Figure(object):
    color = 'white'
    
    def set_color(self, color):
        self.color = color

class Oval(Figure):
    
    def __init__(self, major_axis, minor_axis): 
        self.major_axis = major_axis   
        self.minor_axis = minor_axis

class Square(Figure):
    
    def __init__(self, side): 
        self.side = side   

new_oval = Oval(2, 3)
print('Major axis of oval: ', new_oval.major_axis)
print('Minor axis of oval: ', new_oval.minor_axis)
new_oval.set_color('red')
print('Color of oval: ', new_oval.color)

new_square = Square(4)
print('Side of square: ', new_square.side)
print('Color of square: ', new_square.color)
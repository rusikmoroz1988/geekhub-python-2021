# Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, 
# які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, 
# show_all_information.
#  - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

class Person(object):
    
    def __init__(self, age, name): 
        self.age = str(age)   
        self.name = name
    
    def show_age(self):
        print('Age: ' +  self.age)
    
    def print_name(self):
        print('Name: ' +  self.name)
    
    def show_all_information(self):
        print('All info:')
        self.show_age()
        self.print_name()

first_person = Person(18, 'Vanya')
first_person.show_age()
first_person.print_name()
first_person.show_all_information()
first_person.profession = 'Programmer'
print('Profession: ' + first_person.profession)
    
second_person = Person(55, 'Petya')
second_person.show_age()
second_person.print_name()
second_person.show_all_information() 
second_person.profession = 'Engineer'
print('Profession: ' + second_person.profession)     

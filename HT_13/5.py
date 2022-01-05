# Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки

class Book(object):
    
    def __init__(self, school_class, author, title):
        self.school_class = school_class
        self.author = author
        self.title = title
    
    def __str__(self):
       return f"Book: author --> {self.author}; title --> {self.title}"
    
    def get_school_class(self):
        return self.school_class
    
    def get_author(self):
        return self.author
    
    def get_title(self):
        return self.title
       

class SchoolLibrary(object):
     books = []
     
     def __init__(self, school_address):
        self.school_address = school_address
    
     def add_book(self, librarian, book):
         self.books.append({'librarian': librarian, 'user': None, 'book': book})
     
     def get_book(self, user, book):
         item_list = list(filter(lambda item: item['book'] == book , self.books))
         if len(item_list) == 0:
             print('There is no such book!')
         else:
             self.books.remove(item_list[0])
     
     def return_book(self, librarian, book):
         self.add_book(librarian, book)
     
     def __str__(self):
         return f"School library: address --> {self.school_address}"
         
     
class Librarian(object):
    
    def __init__(self, fio):
        self.fio = fio
    
    def __str__(self):
       return f"Librarian: fio --> {self.fio}"

class User(object):
    
    def __init__(self, fio, school_class):
        self.fio = fio
        self.school_class = school_class
    
    def __str__(self):
       return f"User: fio --> {self.fio}; class --> {self.school_class}"

book_eneida = Book(7, 'Dostoevsky', 'Eneid')
print(book_eneida)
book_romeo = Book(9, 'Shakespeare', 'Romeo and Juliet')
print(book_romeo)
librarian = Librarian('Ostapchuk Petr Vasilievich')
print(librarian)
library = SchoolLibrary('Kiev Khreshchatyk street, 45')
print(library)
user_john = User('John', 7)
print(user_john)
library.add_book(librarian, book_eneida)
library.add_book(librarian, book_romeo)
library.get_book(user_john, book_eneida)
library.return_book(librarian, book_eneida)
library.get_book(user_john, book_romeo)
library.get_book(user_john, book_eneida)
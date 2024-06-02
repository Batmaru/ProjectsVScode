# 1: abstractmethod

# 1. Create a class called Shape with an abstract method called area and another abstract method called
# perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter method.
# 2. Create a class called Shape with an abstract method called area and another abstract method called
# perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter method.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
cerchio1= Circle(radius=10)
print(round(cerchio1.area(),3))


#2: statichmetod 

# Create a class MathOperations with a static method add that takes two numbers and returns their sum,
# and another statichmetod multiply that takes two numbers and returns their product


class MathOperations:
     
    @staticmethod
    def add( n1, n2):
        return n1+n2
    @staticmethod
    def multiply(n1, n2):
        return n1*n2
    
print(MathOperations.add(4,5))
print(MathOperations.multiply(4,5))

# 3: library management system

# Create a book class containing the following attributes: title, author, isbn:
# The book class must contains the following methods:

# __str__ method to return a string representation of the book

# @classmethod from_ string( cls, book_str) to create a bokok instance from a string in the format "title, author, isbn"
# it means that you must use the classreference cls to create a new object of the bok class using a string.

class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def __str__(self)->str:
        return f"title = {self.title}, author = {self.author}, isbn = {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):
        title, author, isbn = book_str.split(', ')
        return cls(title, author, isbn)

        
class Member:
    
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books: list = []
        
    def borrow_book(self, book: str) :
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            return f"the book is already borrowed"
           
        
    def return_book(self, book: str):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            return f"the book is not in the list"
    
    def __str__(self)-> str:
        return f"name = {self.name}, member_id = {self.member_id}"
    
    @classmethod
    
    def from_string(cls, member_str: str):
        name, member_id = member_str.split(', ')
        return cls(name, member_id)
    
class Library:
    
    total_books=0
    
    def __init__(self, books=[], members=[]):
        self.books: list = books
        self.members: list = members
        
    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            Library.total_books+=1
        else:
            return f"the book is already in the list"
        
    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book.title)
            Library.total_books-=1
        else:
            return f"the book is not in the list"
        
    def register_member(self, member):
        if member not in self.members:
            self.members.append(member)
        else:
            return f"the member is already in the list"

    def lend_book(self, book: Book, member: Member):
        if book in self.books and member in self.members:
            self.books.remove(book)
            member.borrowed_books.append(book)
            Library.total_books-=1
            return f"the book is lend to {member.name}"
        else:
            return f"the book is not avalible"
    
    def __str__(self)->str:
        books_list: list=[]
        members_list: list=[]
        for book in self.books:
            books_list.append(book.title)
        for member in self.members:
            members_list.append(member.name)
        
        # if books_list
        return f"Books: {books_list}\nMembers: {members_list}"
    @classmethod
    def library_statics(cls):
        print(f"total books = {cls.total_books}")
        
    
    # Creazione e test delle istanze
book1 = Book("Il nome della rosa", "Umberto Eco", 9780451458765)
book2 = Book.from_string("Il Piccolo Principe, Antoine de Saint-Exupéry, 9780156013987")
member1 = Member("Mario Rossi", 1)
member2 = Member.from_string("Giulia Bianchi, 2")

library1 = Library()
print(library1)  # Output iniziale

library1.add_book(book1)
library1.add_book(book2)
library1.register_member(member1)
library1.register_member(member2)

print(library1)  # Dopo aggiunta di libri e registrazione membri
library1.library_statics()  # Statistiche della libreri

library1.lend_book(book1, member1)

print(library1)  # Dopo prestito libro

library1.library_statics()  # Statistiche della libreri

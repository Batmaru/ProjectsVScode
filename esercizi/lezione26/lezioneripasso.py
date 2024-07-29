# def frequency_dict(elements: list) -> dict:
#     mapdict: dict={}
#     for element in elements:
#         if element not in mapdict.keys():
#             mapdict[element]=1
#         else:
#             mapdict[element]+=1
#     return mapdict
# '''
# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione 
# A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

# For example:'''

# def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
#     A= conditionA
#     B=conditionB
#     C=conditionC
#     if A == True:
#         return 'Operazione permessa'
#     elif B and C == True:
#         return 'Operazione permessa'
#     else:
#         return 'Operazione negata'
    

# '''
# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

# For example:'''    

# def sum_above_threshold(numbers: list[int], threshold: int) -> int:
#     sum=0
#     for n in numbers:
#         if n>20:
#             sum+=n
#     return sum


# '''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con 
# solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.'''
# def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
#     newdict: dict={}
#     for k,v in prodotti.items():
#         if prodotti[k]>20:
#             prodotti[k]-=prodotti[k]*(1/10)
#             newdict[k]=prodotti[k]
#     return newdict

# '''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''
# def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
  
#     for k,v in dict2.items():
#         if k not in dict1.keys():
#             dict1[k]=v
#         else:
#             dict1[k]+=v
#     return dict1
        
# '''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''
# def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
#     newdict={}
#     for tupla in tuples:
#         newdict[tupla[0]]=[]
#         if tupla[0] not in newdict.keys():
#             newdict[tupla[0]]+=[tupla[1]]
#         else:
#             newdict[tupla[0]]+=[tupla[1]]
#     return newdict


# '''Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "admin", la password corrisponde 
# a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".'''

# def check_access(username: str, password: int, is_active: bool) -> str:
#     # cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
#     if username=='admin'and password==12345 and is_active==True:
#         return 'Accesso consentito'
#     return 'Accesso negato'
    
'''Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''
class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_borrowed=False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed=True
            return 'Book borrowed'
        
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed=False
            return 'Book returned'
    
class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
    
    def borrow_book(self, book: Book):
        if book.is_borrowed == False:
            self.borrowed_books.append(book)
            book.is_borrowed =True
        else:
            print('Book is already borrowed')

    def return_book(self, book: Book):
        if book in self.borrowed_books and book.is_borrowed==True:
            self.borrowed_books.remove(book)
            book.is_borrowed =False
        else:
            return 'Book not borrowed'
    

class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str):
        book: Book=  Book(book_id, title, author)
        if book_id not in self.books:
            self.books[book_id]=book
        else:
            return 'Book already exists'
    
    def register_member(self, member_id: str, book_id: str):
        if member_id not in self.members:
            self.members[member_id]=Member(member_id, book_id)
        else:
            return 'Member already exists'
        
    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members:
            if book_id in self.books: 
                if self.books[book_id].is_borrowed==False:
                    self.members[member_id].borrow_book(self.books[book_id])
                else:
                    print('Book is already borrowed')
               
            else:
                print('Book not found')
        else:
            print('Member not found')

    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members:
            if book_id in self.books and self.books[book_id].is_borrowed==True:
               self.members[member_id].return_book(self.books[book_id])
            
            else:
                print('Book not borrowed by this member')
        else:
            return print('Member not found' )       
    def get_borrowed_books(self, member_id)->list[Book]:
        if member_id in self.members:
            listvuota=[]
            listbooks= self.members[member_id].borrowed_books
            for element in listbooks:
                listvuota.append(element.title)
        return listvuota
    

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

library.borrow_book("M001", "B001")
try:
    library.borrow_book("M002", "B001")
except ValueError as e:
    print(e)
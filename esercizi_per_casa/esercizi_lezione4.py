#8-1. Messaggio: scrivi una funzione chiamata display_message() che stampi una frase che racconta a tutti ciò che stai 
# imparando in questo capitolo. Richiama la funzione e assicurati che il messaggio venga visualizzato correttamente.

def display_message()-> None:
    messages: str=("In questo capitolo stiamo imparando a definire e utilizzare funzioni in Python.")
    return messages

print(display_message())
print()

#8-2. Libro preferito: scrivi una funzione chiamata favorite_book() che accetta un parametro, titolo. La funzione dovrebbe 
# stampare un messaggio come "Uno dei miei libri preferiti è Alice nel Paese delle Meraviglie". Chiama la funzione, 
# assicurandoti di includere il titolo di un libro come argomento nella chiamata alla funzione.

def favorite_book(title: str)-> None:
        print(f'my favorite book is: {title}')
        
favorite_book('"the stoic philosphy of Marcus Aurelius"')
print('\n')

#8-3. T-Shirt: Scrivi una funzione chiamata make_shirt() che accetta una taglia e il testo di un messaggio che dovrebbe essere 
# stampato sulla maglietta. La funzione dovrebbe stampare una frase che riassume la taglia della maglietta e il messaggio stampato 
# su di essa. Chiama la funzione una volta utilizzando argomenti posizionali per creare una maglietta. Chiama la funzione una seconda 
# volta utilizzando argomenti chiave.

def make_shirt(size: str, text: str) -> str:
    print(f'the size is {size}, information about this size: {text}')

make_shirt(size='S', text='this size is small')
make_shirt(size='M', text='this size is medium')
print()

#8-4. Camicie grandi: modifica la funzione make_shirt() in modo che le camicie siano grandi per impostazione predefinita con un messaggio
# che dice I love Python. Crea una maglietta grande e una media con il messaggio predefinito e una maglietta di qualsiasi taglia con 
# un messaggio diverso.

def make_shirt_modified(product: str, size: str) -> None:
    if product == 'camicia':
        print("La camicia è di taglia L e il messaggio è 'I love Python'.")
    elif product == 'maglietta':
        if size == 'L':
            print("La maglietta è di taglia L, questa taglia non è disponibile per le magliette.")
        elif size == 'M':
            print("La maglietta è di taglia M, questa taglia non è disponibile per le magliette.")
        else:
            print(f"La maglietta è di taglia {size} sei fortunato\a questa taglia è disponibile.")
    else:
        print(f'il\la {product},è disponibile in qualsiasi taglia.')


make_shirt_modified('maglietta', 'S')
make_shirt_modified('pantalone', 'S')



#8-5. Città: scrivi una funzione chiamata description_city() che accetta il nome di una città e del suo paese. La funzione 
# dovrebbe stampare una frase semplice, come Reykjavik è in Islanda. Assegnare al parametro per il paese un valore predefinito.
# Chiama la tua funzione per tre città diverse, almeno una delle quali non è nel Paese predefinito.

def description_city(city: str, country: str = "Italia") -> None:
    print(f"{city} si trova in {country}.")

description_city("Roma")
description_city("New York", "Stati Uniti")
description_city("Tokyo", "Giappone")
print()

#8-6. Nomi di città: scrivi una funzione chiamata city_country() che accetta il nome di una città e del suo paese. La funzione dovrebbe 
# restituire una stringa formattata in questo modo: "Santiago, Cile". Chiama la tua funzione con almeno tre coppie città-paese e stampa 
# i valori restituiti.

def city_country(city: str, country: str):
    print(f"{city}, {country}")
    
city_country("Roma", "Italia")
city_country("New York", "Stati Uniti")
city_country("Tokyo", "Giappone")
print()

#8-7. Album: scrivi una funzione chiamata make_album() che costruisce un dizionario che descrive un album musicale. La funzione dovrebbe 
# includere il nome dell'artista e il titolo dell'album e dovrebbe restituire un dizionario contenente queste due informazioni. Utilizza 
# la funzione per creare tre dizionari che rappresentano album diversi. Stampa ciascun valore restituito per mostrare che i dizionari 
# memorizzano correttamente le informazioni sull'album. Utilizza None per aggiungere un parametro facoltativo a make_album() che ti consente 
# di memorizzare il numero di brani su un album. Se la riga chiamante include un valore per il numero di brani, aggiungi tale valore al dizionario 
# dell'album. Effettua almeno una nuova chiamata di funzione che includa il numero di brani di un album.

def make_album(name: str, title: str, songs: int=None)->dict[str,str,int]:
    artist_dict: dict={
        'artist': name,
        'album_title': title
        }
    if songs is not None:
        artist_dict['num_songs']=songs
    return artist_dict

album1 = make_album('Michael Jackson', 'Thriller')
album2 = make_album('The Beatles', 'Abbey Road')
album3 = make_album('Pink Floyd', 'The Dark Side of the Moon', 10)
album4 = make_album('Queen', 'A Night at the Opera')
album5 = make_album('Led Zeppelin', 'Led Zeppelin IV', 8)

print(album1)
print(album2)
print(album3)
print(album4)
print(album5)
print()

#8-8. Album utente: inizia con il tuo programma dall'esercizio 8-7. Scrivi un ciclo while che consenta agli utenti di inserire l'artista e il 
# titolo di un album. Una volta ottenute queste informazioni, chiama make_album() con l'input dell'utente e stampa il dizionario creato. Assicurati 
# di includere a 'quit value' nel ciclo while.
# def make_album1(name: str, title: str, songs: int=None) -> dict:
#     artist_dict = {
#         'artist': name,
#         'album_title': title
#     }
#     if songs is not None:
#         artist_dict['num_songs'] = songs
#     return artist_dict

# artist = ''
# songs = ''
# while artist.lower() != 'quit':
  
#     while True:   
#         artist = input("Inserisci il nome dell'artista (o 'quit' per uscire): ")
#         if artist.isalpha():
#             artist=str(artist)
#             break
            
#         else:
#             print('errore questo non è un nome')
#             continue
#     if artist.lower() == 'quit':
#                 break
#     else:   
#         title = input("Inserisci il titolo dell'album: ")

#         while True:
#             songs=input("inserisci il numero delle canzoni (se non c'è questa informazione non inserire): ")
#             if songs!='':
#                 if songs.isdigit():
#                         songs=int(songs)
#                         break
#                 else:
#                     print('errore questo non è un numero')
#                     continue
#             else:
#                 songs=None
#                 break
#     print(make_album1(artist, title, songs))
    
# print()


#8-9. Messaggi: crea un elenco contenente una serie di brevi messaggi di testo. Passa l'elenco a una funzione chiamata show_messages(), 
# che stampa ogni messaggio di testo.
messages = [
    "Ciao! Come stai?",
    "Buongiorno a tutti!",
    "Non vedo l'ora di iniziare!",
    "Hai finito il compito?",
    "Ricordati di fare la spesa.",
    "Il tempo oggi è fantastico!",
    "Sto imparando Python e mi diverto un sacco!",
    "Buon lavoro a tutti!",
    "Sono così felice oggi!",
    "Domani è un nuovo giorno pieno di opportunità!",
    "Ti auguro una giornata fantastica!"
]

def show_messages(lista: list)->str:
    for phrase in lista:
        print(f'{phrase}')
        
show_messages(messages)
print()

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each 
# text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your 
# lists to make sure the messages were moved correctly.

def send_messages(lista: list)->list:
    sent_messages: list=[]
    for phrase in lista:
        sent_messages.append(phrase)
    print(f'la lista è: {lista}\n')
    print(f'la lista copiata è: {sent_messages}\n')

send_messages(messages)    
print()

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

def send_messages(lista: list)->list:
    sent_messages: list=[]
    for phrase in lista:
        sent_messages.append(phrase)
    return sent_messages

copy_messages=send_messages(messages.copy())
print(f'la lista originale è: {messages}\n')
print(f'la copia della lista è: {copy_messages}')
print()

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects 
# as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
# using a different number of arguments each time.

def sandwich(name:str, ingredients: list)->dict[str, list]:
    person_dict={
        'name': name,
        'ingredients':ingredients
    }
    print(f"gli ingredienti del panino di {person_dict['name']} sono: {person_dict['ingredients']}")


sandwich('Marco', ['Prosciutto', 'Formaggio'])
sandwich('Giulia', ['Salame', 'Mozzarella', 'Pomodoro'])
sandwich('Luca', ['Pollo', 'Insalata', 'Maionese', 'Pomodoro'])
print()

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that 
# describe you. All the values must be passed to the function as parameters. The function then must return stra string such as "Eric Crow, age 45, 
# hair brown, weight 67"

def build_profile(fullname: str, age: int, hair: str, eyes: str)-> str:
    personal_dict:dict={
        'name' : fullname,
        'age' : age,
        'color hair' : hair,
        'color eyes': eyes
        }
    print(f'{personal_dict["name"]}, {personal_dict["age"]} years old, {personal_dict["color hair"]}, {personal_dict["color eyes"]}')
    
build_profile('Marwan Rafik', 19, 'black hair', 'black eyes')

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such 
# as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# Print the dictionary that’s returned to make sure all the information was stored correctly. 

def make_car(manufacturer: str, model: str, color=None, tow_package=False) -> dict:
    car_info = {
        'manufacturer': manufacturer,
        'model': model,
        'color': color,
        'tow_package': tow_package
    }
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
print()

#8.16
import sandwich_function
from sandwich_function import sandwich
from sandwich_function import sandwich as fn
import sandwich_function as mn
from sandwich_function import *

print()

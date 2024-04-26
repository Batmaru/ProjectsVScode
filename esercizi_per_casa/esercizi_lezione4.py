#8-1. Messaggio: scrivi una funzione chiamata display_message() che stampi una frase che racconta a tutti ciò che stai 
# imparando in questo capitolo. Richiama la funzione e assicurati che il messaggio venga visualizzato correttamente.

def display_message():
    print("In questo capitolo stiamo imparando a definire e utilizzare funzioni in Python.")

display_message()
print()

#8-2. Libro preferito: scrivi una funzione chiamata favorite_book() che accetta un parametro, titolo. La funzione dovrebbe 
# stampare un messaggio come "Uno dei miei libri preferiti è Alice nel Paese delle Meraviglie". Chiama la funzione, 
# assicurandoti di includere il titolo di un libro come argomento nella chiamata alla funzione.

def favorite_book(title: str):
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




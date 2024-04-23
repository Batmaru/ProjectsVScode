def substract_all(x: list[float], y: float) -> list[float]:
    result: list[float] = []
    for numbers in x:
        result.append(numbers-y)
    return result




mylist: list[float] = [1,2,3,4,5]
x: float = 10
result = substract_all(mylist,x)
print(result)

#sottrazioni con liste

def substract_list(x: list[float], y: float) -> list[float]:
    if len(x)!=len(y):
        print('entrambe le liste devono avere almeno un elemento')
        return None
    
    risultati = []
    for elem1,elem2 in zip(x,y):
        risultato=elem1-elem2
        risultati.append(risultato)
    return risultati
    

mylist: list[float] = [1,2,3,4,5]
x: float = [2,3,4,5,6]
result = substract_list(mylist,x)
print(result)

#sottrazioni con liste con lunghezz differente
def substract_list(x: list[float], y: float) -> list[float]:
    risultati = []
    if len(x)>=len(y):
        for i in range(len(y)):
            diff = x[i]-y[i]
            risultati.append(diff)
    else:
        for i in range(len(x)):
            diff = x[i]-y[i]
            risultati.append(diff)
    return risultati
    

mylist: list[float] = [5,2,3,4,5,6]
x: float = [2,3,4,5,6]
result = substract_list(mylist,x)
print(result)

#sottrazioni con liste con lunghezz differente
def add_diff_to_res(x: list[float], y: list[float], lenght: int)-> list [float]:
    res: list[float] = []
    for i in range(lenght):
        diff = x[i] - y[i]
        res.append(diff)
    return res
def substract_list(x: list[float], y: float) -> list[float]:
   length = min(len(x), len(y))
   res: list[float]= add_diff_to_res(x,y, length)
   return res
    

mylist: list[float] = [5,2,3,4,5,6]
x: float = [2,3,4,5,6]
result: list[float] = substract_list(mylist,x)
print(f'il risultato dopo la sottrazione è{result}')

import re
s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica,[2] dove le precedenti teorie classiche risultano inadeguate .Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione[3] e la materia[4] sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella,[5] è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg.[6] Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
def counter(s: str) -> list[int]:
    num_caratteri: int= len(s)
    parole:int =s.split()
    num_parole: int=len(parole)
    parole_distinte: int= len(set(parole))
    frasi: int= re.split(r'[.!?]',s)
    num_frasi: int= len(frasi)-1
    lista_risultati: int=[num_caratteri, num_parole, parole_distinte, num_frasi]
    return lista_risultati  

print("risultato dell'analisi della stringa:",counter(s))

def word_count(s: str) -> dict:
    # Rimuovi i caratteri di punteggiatura e converti tutte le parole in minuscolo
    cleaned_words = ''.join(char.lower() if char.isalnum() or char.isspace() else '' for char in s)

    words = cleaned_words.split()

    word_count_dict = {}
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


print(word_count(s))
print()

def word_count2(s: str) -> dict:
    # Usa la tua funzione per contare tutte le parole
    word_count_dict = word_count(s)
    
    # Filtra solo le parole che compaiono più di una volta
    filtered_word_count_dict = {word: count for word, count in word_count_dict.items() if count > 1}

    return filtered_word_count_dict

print(word_count2(s))
print()


def is_palindrome(s: str) -> bool:
    
    s = s.replace(" ", "").lower()
    
    
    start = 0
    end = len(s) - 1
    
 
    while start < end:
       
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    # Se si esce dal ciclo, significa che la stringa è palindroma
    return True

# Esempi di utilizzo
print(is_palindrome("amo roma"))  # True
print(is_palindrome("ciao come stai?"))  # False

#Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i 
# tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!

#Qual è il problema?
#Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che 
#cerca di confondersi tra la folla (t). Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai 
#il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe 
#(l'ordine cambia).
#Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. 
#Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti 
#restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!2
def is_subsequence(s: str, t: str) -> bool:
    cont_s=0
    cont_t=0
    while cont_t<len(t) and cont_s<len(s):
        if s[cont_s] == t[cont_t]:
            cont_s+=1
        cont_t+=1
    return cont_s==len(s)
    

print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("cba",'fdidfavjocdfionab'))
print()

#Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). Questi gioielli hanno 
# vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
#Qual è la svolta?
#Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti,
# ovvero gioielli con valori unici.
#Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti 
# almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.
#Ma c'è un problema!
#Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), 
# la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(nums: list[int]) -> int:
    i=0
    if not nums:
        return None
    l_no_multiples: list=[]
    for n in nums:
        if n not in l_no_multiples:
            l_no_multiples.append(n)
    if len(l_no_multiples)>=3:
        return l_no_multiples[2]
    else:
        return max(l_no_multiples)

print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))
print(third_max([4, 5, 5, 6, 6, 6]))   
print(third_max([1, 2, 3, 4, 5]))      
print(third_max([5, 5, 5, 5, 5]))      
print(third_max([1, 1, 2, 2, 3, 3]))  
print(third_max([1, 2, 3, 4, 4, 4]))   
print(third_max([2, 2, 2, 2, 2, 2]))   
print(third_max([1]))                  
print(third_max([])) 
print()                  

# Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi.
# Queste note possono avere altezze (valori) diversi.
# Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la 
# nota massimale e quella minimale è uguale a 1.
# Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.

# Trovare l'armonia perfetta:

# Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri).
# La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note.
# Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

# Colpire le note giuste:

# Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3].
# La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

# For example:

# Test	Result
# print(find_lhs([1,3,2,2,5,2,3,7]))
# print(find_lhs([1,2,3,4]))

def find_lhs(nums: list[int]) -> list[int]:
    fnums_dict: dict[int,int]= {}
    for n in nums:
        if n in fnums_dict:
            fnums_dict[n]+=1
        else:
            fnums_dict[n]=1
    max_lenght=0
    for n in fnums_dict:
        if n+1 in fnums_dict:
            max_lenght=max(max_lenght, fnums_dict[n]+fnums_dict[n+1])
    return max_lenght

print(find_lhs([1,3,2,2,5,2,3,7]))
print(find_lhs([1,2,3,4]))



    



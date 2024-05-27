import random


print("BANG !!!!! AND THEY'RE OFF !!!!")
lista_percorso: list=[ "_" for n in range (1,71)]
posizione_tartaruga: str= "T"
posizione_lepre: str= "H"
lista_tartaruga: list= lista_percorso
lista_tartaruga.pop(0)
lista_tartaruga.insert(0,posizione_tartaruga)
lista_lepre: list=lista_percorso
lista_lepre.pop(0)
lista_lepre.insert(0,posizione_tartaruga)


"""nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento"
 quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole."""


def calcola_tartaruga(lista_tartaruga: list):
    """Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, 
        nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o 
        un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole."""
    
    n_random: int=  random.randint(1,10)
    print(lista_tartaruga)
    if 1<=n_random<=5:
        posizioneT = lista_tartaruga.index("T")
        lista_tartaruga.pop(posizioneT)
        lista_tartaruga.insert(posizioneT, "_")
        nuova_posizioneT = posizioneT+3
        lista_tartaruga.pop(nuova_posizioneT)
        lista_tartaruga.insert(nuova_posizioneT, posizione_tartaruga)

        #scivolata
    elif 6<= n_random<=7:
        index=lista_tartaruga.index("T") 
        if index- 6 <0:
            lista_tartaruga.pop(index)
            lista_tartaruga.insert(index,"_")
            lista_tartaruga.pop(0)
            lista_tartaruga.insert(0, posizione_tartaruga)
        else:
            posizioneT=lista_tartaruga.index("T")
            posizioneTdopo=posizioneT-6
            lista_tartaruga.pop(posizioneT)
            lista_tartaruga.insert(posizioneT,"_")
            lista_tartaruga.pop(posizioneTdopo)
            lista_tartaruga.insert(posizioneTdopo,"T")
    elif 8<= n_random<=10:
        posizioneT=lista_tartaruga.index("T")
        posizioneTdopo=posizioneT+1
        lista_tartaruga.pop(posizioneT)
        lista_tartaruga.insert(posizioneT,"_")
        lista_tartaruga.pop(posizioneTdopo)
        lista_tartaruga.insert(posizioneTdopo,"T")
    
    return lista_tartaruga

print(calcola_tartaruga(lista_tartaruga))


            
        
        
        

        

   
# tick: int= 0
# if tick == 0:
#     lista_tartaruga.pop(0)
#     lista_tartaruga.insert(0,posizione_tartaruga)
#     lista_lepre.pop
#     lista_lepre.insert(0, posizione_lepre)
#     tick+=1
# else:
#     while lista_tartaruga.index("T")>= len(lista_percorso-1) or lista_tartaruga.index("H")>= len(lista_percorso-1):
        


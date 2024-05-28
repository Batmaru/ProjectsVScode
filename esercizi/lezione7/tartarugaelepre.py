import random

lista_percorso: list=[ "_" for n in range (1,71)]
posizione_tartaruga: str= "T"
posizione_lepre: str= "H"
lista_tartaruga: list= [ "_" for n in range (1,71)]
lista_tartaruga.pop(0)
lista_tartaruga.insert(0,posizione_tartaruga)
lista_lepre: list=[ "_" for n in range (1,71)]
lista_lepre.pop(0)
lista_lepre.insert(0,posizione_lepre)



"""nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento"
 quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole."""


def calcola_tartaruga(lista_tartaruga: list):
    """Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, 
        nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o 
        un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole."""
    
    n_random: int=  random.randint(1,10)

    #passo veloce
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

            #passo lento
    elif 8<= n_random<=10:
        posizioneT=lista_tartaruga.index("T")
        posizioneTdopo=posizioneT+1
        lista_tartaruga.pop(posizioneT)
        lista_tartaruga.insert(posizioneT,"_")
        lista_tartaruga.pop(posizioneTdopo)
        lista_tartaruga.insert(posizioneTdopo,"T")
    
    return lista_tartaruga



def calcola_lepre(lista_lepre: list):
    """- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1."""


    """1<=i<=2 (+0) = riposo, 3<=i<=4 = grande balzo(+9), i=5 = grande scivolata(-12, se la T ha posizione minore di 12, T torna in posizione 1), 
    6<=i<=8 = piccolo_balzo(+1), 9<=i<=10 = piccola scivolata (-2, ma non meno di posizione 1)"""
    n_random = random.randint(1,10)
    #riposo
    if 1<=n_random<=2:
        return lista_lepre
    
    #grande balzo
    elif 3<=n_random<=4:
        posizioneL=lista_lepre.index("H")
        posizioneLdopo=posizioneL+9
        lista_lepre.pop(posizioneL)
        lista_lepre.insert(posizioneL,"_")
        lista_lepre.pop(posizioneLdopo)
        lista_lepre.insert(posizioneLdopo,"H")
    
    #grande scivolata
    elif n_random==5:
        posizioneL=lista_lepre.index("H")

        if posizioneL>12:
            posizioneLdopo=posizioneL-12
            lista_lepre.pop(posizioneL)
            lista_lepre.insert(posizioneL,"_")
            lista_lepre.pop(posizioneLdopo)
            lista_lepre.insert(posizioneLdopo,"H")
        else:
            lista_lepre.pop(posizioneL)
            lista_lepre.insert(posizioneL,"_")
            lista_lepre.pop(0)
            lista_lepre.insert(0,"H")
    
    #piccolo balzo
    elif 6<=n_random<=8:
        posizioneL=lista_lepre.index("H")
        posizioneLdopo=posizioneL+1
        lista_lepre.pop(posizioneL)
        lista_lepre.insert(posizioneL,"_")
        lista_lepre.pop(posizioneLdopo)
        lista_lepre.insert(posizioneLdopo,"H")
    
    #piccola scivolata
    elif 9<=n_random<=10:
        posizioneL=lista_lepre.index("H")
        if posizioneL>1:
            posizioneLdopo=posizioneL-2
            lista_lepre.pop(posizioneL)
            lista_lepre.insert(posizioneL,"_")
            lista_lepre.pop(posizioneLdopo)
            lista_lepre.insert(posizioneLdopo,"H")
        else:
            lista_lepre.pop(posizioneL)
            lista_lepre.insert(posizioneL,"_")
            lista_lepre.pop(0)
            lista_lepre.insert(0,"H")

    return lista_lepre


        
t1=True
t2=True
tick: int= 0
if tick == 0:
    print("BANG !!!!! AND THEY'RE OFF !!!!")
    lista_tartaruga.pop(0)
    lista_tartaruga.insert(0,posizione_tartaruga)
    lista_lepre.pop
    lista_lepre.insert(0, posizione_lepre)
    tick+=1
while t1==True:
        while t2==True:
            lista_tartaruga=calcola_tartaruga(lista_tartaruga)
            lista_lepre=calcola_lepre(lista_lepre)
            tick+=1

            if lista_tartaruga.index("T")> lista_lepre.index("H"):
                print("TARTARUGA IS IN THE LEAD !!!!")

            elif lista_tartaruga.index("T")< lista_lepre.index("H"):
                print("LEPRE IS IN THE LEAD !!!!")  

            elif lista_tartaruga.index("T")== lista_lepre.index("H") and lista_tartaruga.index:
                lista_lepre_ouch= [n for n in lista_lepre]
                lista_tartaruga_ouch=[n for n in lista_tartaruga]
                posizioneL= lista_lepre_ouch.index("H")
                posizioneT= lista_tartaruga_ouch.index("T")
                lista_lepre_ouch.pop(posizioneL)
                lista_lepre_ouch.insert(posizioneL,"Ouch")
                lista_tartaruga_ouch.pop(posizioneT)
                lista_tartaruga_ouch.insert(posizioneT,"Ouch")
                print(f'posizione tartaruga: {lista_tartaruga_ouch}, \n\n posizione lepre{lista_lepre_ouch}')
            
            elif lista_tartaruga.index("T") == lista_lepre.index("H") and lista_tartaruga.index("T")>=70:
                t2=False
                print ("IT'S A TIE !!!!")
            
            elif lista_tartaruga.index("T")>=70 and lista_lepre.index("H")<=70:
                t2=False
                print ("TARTARUGA WINS !!!!")
            elif lista_lepre.index("T") >= 70 and lista_tartaruga.index("H"):
                t2=False
                print ("LEPRE WINS !!!!")
        t1=False
            

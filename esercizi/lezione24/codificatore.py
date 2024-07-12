from abc import ABC, abstractmethod

class CodificatoreMessaggi(ABC):
    
    @abstractmethod
    def codifica(self, testocodificato: str)->str:
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato: str)->str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggi, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave=chiave

    def codifica(self, testoinchiaro: str):
        alfabetostr = 'abcdefghijklmnopqrstuvwxyz'
        testoinchiaro=testoinchiaro.lower()
        listacodifica = []
        
        for element in testoinchiaro:
            if element in alfabetostr:
                elementalfindex = alfabetostr.index(element)
                new_index = (elementalfindex + self.chiave) 
                if new_index<=len(alfabetostr):
                    listacodifica.append(alfabetostr[new_index])
                else:
                    new_index=new_index-len(alfabetostr)
                    listacodifica.append(alfabetostr[new_index])

            else:
                listacodifica.append(element)
                
        
        return ''.join(listacodifica)
    

    def decodifica(self, testoinchiaro: str):
        alfabetostr = 'abcdefghijklmnopqrstuvwxyz'
        testoinchiaro=testoinchiaro.lower()
        listacodifica = []
        
        for element in testoinchiaro:
            if element in alfabetostr:
                elementalfindex = alfabetostr.index(element)
                new_index = (elementalfindex - self.chiave) 
                if new_index>=0:
                    listacodifica.append(alfabetostr[new_index])
                else:
                    new_index=new_index+len(alfabetostr)
                    listacodifica.append(alfabetostr[new_index])

            else:
                listacodifica.append(element)
                
        
        return ''.join(listacodifica)

class Cifratoreacombinazione(CodificatoreMessaggi):
    def __init__(self, numero: int):
        self.numero=numero

    def codifica(self, testoinchiaro:str):
        testoinchiaro=testoinchiaro.lower()
        numerocicli=1
        while numerocicli<=self.numero:
            if len(testoinchiaro)%2!=0:
                lunghezzastringacorta=len(testoinchiaro)//2
                lunghezzastringalunga=lunghezzastringacorta+1
                stringalunga=''
                stringacorta=''
                for n in range(0,lunghezzastringalunga):
                    stringalunga+=testoinchiaro[n]
                for n in range(lunghezzastringalunga,len(testoinchiaro)):
                    stringacorta+=testoinchiaro[n]
                for n in range(0,lunghezzastringacorta):
                    testoinchiaro=''+ lunghezzastringalunga[n]
                    testoinchiaro+= lunghezzastringacorta[n]
                    if n==len(lunghezzastringacorta):
                        testoinchiaro+= lunghezzastringalunga[n+1]
                return testoinchiaro
            else:
                lunghezzastringa=len(testoinchiaro)//2
                stringa1=''
                stringa2=''
                for n in range(0,lunghezzastringa):
                    stringa1+=testoinchiaro[n]
                for n in range(lunghezzastringa,len(testoinchiaro)):
                    stringa2+=testoinchiaro[n]
                for n in range(0,lunghezzastringa):
                    testoinchiaro=''+stringa1[n]
                    testoinchiaro+= stringa2[n]
                return testoinchiaro
                




            

                    






    

chiave1=CifratoreAScorrimento(5)

print(chiave1.codifica('ciaoZ'))
print(chiave1.decodifica('abctG'))

numero1=Cifratoreacombinazione(3)

print(numero1.codifica('asdrubale'))
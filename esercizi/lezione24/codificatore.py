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
      
        while self.chiave>len(alfabetostr):
            self.chiave=self.chiave-len(alfabetostr)      
        for element in testoinchiaro:
            if element in alfabetostr:
                elementalfindex = alfabetostr.index(element)
                new_index = (elementalfindex + self.chiave) 
                if new_index<len(alfabetostr):
                    listacodifica.append(alfabetostr[new_index])
                else:
                    new_index=new_index-len(alfabetostr)
                    listacodifica.append(alfabetostr[new_index])
                
        
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

class CifratoreACombinazione(CodificatoreMessaggi, DecodificatoreMessaggio):
    def __init__(self, numero: int):
        self.numero=numero

    def codifica(self, testoinchiaro:str):
        testoinchiaro=testoinchiaro.lower()
        lentestoinchiaro=len(testoinchiaro)
        numerocicli=1
        tuttelecodifiche: list=[]
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
                testoinchiaro=''
                for n in range(0,lunghezzastringacorta):
                    testoinchiaro+= stringalunga[n]
                    testoinchiaro+= stringacorta[n]
                    if len(testoinchiaro)==lentestoinchiaro-1:
                        testoinchiaro+= stringalunga[n+1]
                        tuttelecodifiche.append(testoinchiaro)
                        numerocicli+=1
                        
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
                    tuttelecodifiche.append(testoinchiaro)
                    numerocicli+=1
        return f'le codifiche sono: {tuttelecodifiche}, quella finale è {testoinchiaro}'
    
    def decodifica(self, testoinchiaro: str):
        testoinchiaro=testoinchiaro.lower()
        numerocicli=1
        tuttelecodifiche: list=[]
        while numerocicli<=self.numero:
    
            lunghezzastringa=len(testoinchiaro)
            stringa1=''
            stringa2=''
            for n in range(0,lunghezzastringa):
                if n%2==0:
                    stringa1+=testoinchiaro[n]
                else:
                    stringa2+=testoinchiaro[n]
            testoinchiaro=stringa1+stringa2
            tuttelecodifiche.append(testoinchiaro)
            numerocicli+=1
        return f'le codifiche sono: {tuttelecodifiche}, quella finale è {testoinchiaro}'


                
                    





            

                    






    

chiave1=CifratoreAScorrimento(2)

print(chiave1.codifica('abcdefghijklmnopqrstuvwxyz'))
print(chiave1.decodifica('cdefghijklmnopqrstuvwxyzab'))

numero1=CifratoreACombinazione(4)

print(numero1.codifica('asdrubale'))
print(numero1.decodifica('auerldasb'))
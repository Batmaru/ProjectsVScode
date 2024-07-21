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
        return testoinchiaro
    
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
            
            
        return testoinchiaro


                
                    





            

                    





if __name__ == "__main__":
    

    chiave1=CifratoreAScorrimento(2)
    with open("esercizi\lezione24\example.txt", 'w', encoding='utf-8') as file:
        file.write('ciao io sono marwan rafik, sono bellissimo e ho 20 anni')

    with open("esercizi\lezione24\example.txt", 'r', encoding='utf-8') as file:
        file1=file.read()

    filecodificato = chiave1.codifica(file1)
    print(filecodificato)
    print(chiave1.decodifica(filecodificato))

    numero1=CifratoreACombinazione(4)
    
    with open("esercizi\lezione24\examplecifratoreacombinazione.txt", 'w', encoding='utf-8') as file:
        file.write('ciao io sono marwan rafik, sono bellissimo e ho 20 anni')

    with open("esercizi\lezione24\examplecifratoreacombinazione.txt", 'r', encoding='utf-8') as file:
        file2=file.read()

    print(f'il testo letto è: {file2}')
    filecodificato1 = numero1.codifica(file2)
    print(f'la codifica è: {filecodificato1}')
    print(f'la decodifcia è: {numero1.decodifica(numero1.codifica(file2))}')
class Documento:
    def __init__(self):
        self.testo: str = ''

    def getText(self)->str:
        return self.testo
    
    def setText(self, testo:str):
        self.testo = testo

    def isInText(self, parola: str)->bool:
        parole: list=[p for p in self.testo.split()]
        if parola in parole:
            return True
        else:
            return False
        
class Email(Documento):
    def __init__(self):
        super().__init__()
        self.mittente: str =''
        self.destinatario: str =''
        self.titolo: str = ''

    def getMittente(self):
        return self.mittente
    
    def setMittente(self, mittente: str):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, destinatario: str):
        self.destinatario = destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setTitolo(self, titolo: str):
        self.titolo = titolo

    def getText(self) -> str:
        testoemail: str= f"Da: {self.getMittente()} A: {self.getDestinatario()}\nTitolo: {self.getTitolo()}\nMessaggio: {self.testo}"
        return testoemail
    
    def writetofile(self, percorso:str):
        file = open(percorso, 'w')
        file.write(self.getText())
        file.close()
        
    
class File(Documento):
    def __init__(self, nomePercorso):
        super().__init__()
        self.nomePercorso: str=nomePercorso

    def leggiTestoDaFile(self):
        file = open(self.nomePercorso, 'r')
        self.setText(file.read())
        file.close()
        
    def getText(self):
        filebello = f'Percorso: {self.nomePercorso}\nContenuto: {self.testo}'
        return filebello
    


        
    
        
    

documento1: Documento=Documento()
documento1.setText('ciao sono mario')
email=Email()
email.setMittente('marwan@gmail.com')
email.setDestinatario('mario@gmail.com')
email.setTitolo('ti scrivo per chiedere come stai')
email.setText('Questo è il contenuto del file')
email.getText()
email.writetofile('/home/user/ProjectsVScode/esercizi/lezione19/documento.txt')
file1=File('/home/user/ProjectsVScode/esercizi/lezione19/documento.txt')
file1.leggiTestoDaFile()
print(file1.getText())



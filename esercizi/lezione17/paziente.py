from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name:str, last_name: str, code: str):
        super().__init__(first_name, last_name)
        self.__code: str = code
    
    def setIdCode(self, codice:str):
        if type(codice)==str:
            self.__code = codice
        else:
            print('il codice inserito non è un a stringa')
    
    def getIdCode(self):
        return self.__code
    
    def patientInfo(self):
        name=self.GetName()
        codice= self.getIdCode()
        return (f'Paziente: {name} {self.GetLastName()},\nCodice id: {codice}')
    


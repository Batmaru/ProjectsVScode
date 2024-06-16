from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)
        if type(specialization)==str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            raise TypeError("Specialisation must be a string")
        
        if type(parcel)==float:   
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("la parcella deve essere un float")
    
    def setparcel(self, n):
        if type(n)==float:
            self.__parcel = n
        else:
            print("la parcella deve essere un float")
    
    def setspecialization(self, s: str):
        if type(s)==str:
            self.__specialization = s
        else:
            print("la specializzazione deve essere una stringa")
    
    def getparcel(self):
        return self.__parcel
    
    def getspecialization(self):
        return self.__specialization
        
    def Doctorgreet(self):
        stringa = self.greet()
        specialization= self.getspecialization()
        parcel = self.getparcel()
        return stringa+ f", sono specializzato in: {specialization}, il mio stipendio è: {parcel}"
    
    def isValidDoctor(self):
        age= self.GetAge()
        name = self.GetName()
        last_name = self.GetLastName()
        if age>=30:
            print(f'il dottor: {name} {last_name}, è un dottore valido')
            return True
        else:
            print(f'il dottor: {name} {last_name}, non è un dottore valido')
            return False
        

        

dottore1= Dottore('marwan', 'boh', 'cardio chirurgo', 29.00)
dottore2= Dottore('davide','trischitta','chirurgo plastico', 400.32)
dottore1.SetAge(34)
dottore2.SetAge(12)
print(dottore1.Doctorgreet())
print(dottore2.Doctorgreet())
dottore1.isValidDoctor()
dottore2.isValidDoctor()  
        


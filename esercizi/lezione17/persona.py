class Persona:
    def __init__(self, first_name: str, last_name: str):
        # if instance(first_name,str):
        #   self.__first_name=first_name
        # else:
        #   print("first_name must be a string")
        if type(last_name) and type(first_name)== str:
            self.__last_name= last_name
            self.__first_name = first_name
            self.__age: int = 0
        else:
            self.__last_name= None
            self.__first_name = None
            self.__age: int = None
            print("Il nome e il cognome devono essere stringhe")
    
    
    def SetName(self, first_name)->str:
        if type(first_name) == str:
            self.__first_name = first_name
        else:
            print("Il nome deve essere una stringa")

    def SetLastName(self, last_name)->str:
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            print("Il cognome deve essere una stringa")

    def SetAge(self, età: int)->int:
        if type(età) == int:
            self.__age = età
        else:
            print("L'età deve essere un numero intero")
        
    def GetName(self):
        return self.__first_name
                
    def GetLastName(self):
        return str(self.__last_name)
    
    def GetAge(self):
        return self.__age
    
    def greet(self):
        name=self.GetName()
        surname=self.GetLastName()
        age=self.GetAge()
        return (f"Ciao, mi chiamo {name} {surname}, ho {age} anni")



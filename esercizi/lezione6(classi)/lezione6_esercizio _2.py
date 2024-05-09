class Student:

    def __init__(self, name: str,studyProgram: str, age: int,gender: str):
        self.name = name
        self.studyProgram = studyProgram  
        self.age = age
        self.gender=gender
        
    
    def __str__(self)->str:
            return (f'{self.name} is studying {self.studyProgram}, he is {self.age}, he/she is a/an {self.gender} ')
    
    def printInfo(self):
         return self.__str__()
    
Marwan = Student('marwan', 'python', 19, 'man')
Marco= Student('marco', 'python', 23, 'man')
Silviu= Student('silviu','python', 23, 'optimusprime')

print(Marwan)
print(Marco.printInfo())
print(Silviu.printInfo())
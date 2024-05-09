class Animal:
    def __init__(self, name: str, family: str, legs= int):
        self.name = name
        self.family = family
        self.legs = legs
    
    def setLegs(self,legs):
        self.legs = legs

    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(f'Name: {self.name}, Family: {self.family}, legs: {self.legs}')



animal1= Animal( name='cat', family='feline', legs= 4)
animal2= Animal(name= 'dog', family='canine', legs=4)

print(f'animal1: {animal1.name}')
print(f'animal2: {animal2.name}')

animal1.legs=3
animal2.setLegs(6)

print(f'legs of animal1: {animal1.getLegs()}' )
print(f'legs of animal2: {animal2.getLegs()}' )
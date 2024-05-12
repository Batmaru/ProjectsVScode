class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby: set[str]=set()
    
    def bulk_set_hobby(self, new_hobbies: list[str]):
        for hobby in new_hobbies:
            self.set_hobby(hobby)
            # piu efficaciemente self.hobby += new_hobbies
    
    def set_hobby( self, new_hobby: str):
        self.hobby.add(new_hobby)

    def __str__(self)-> str:
        if self.hobby:
            return (f"{self.name} is {self.age} years old, his hobby/ies = {self.hobby}")
        else:   
            return (f"{self.name} is {self.age} years old")
     
    def __remove_hobby__ (self, old_hobby: str):
        if old_hobby in self.hobby:
            self.hobby.remove(old_hobby)



#creazione di oggetti

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
silviu = Person( "Silviu", 20)
davide = Person("Davide", 50)
marco = Person("Marco", 45)

#un po di operazioni con le funzioni all'interno della classe
alice.set_hobby('calcio')
alice.bulk_set_hobby(['cucinare'])
alice.__remove_hobby__('cucinare')
print(alice.__str__())

print(alice.hobby)

#nome
print(bob.age)

#operazini
if bob.age>alice.age:
    print(f"Bob is older than Alice, he is {bob.age}")

else:
    print(f"Alice is older than Bob, she is {alice.age}")

#operazioni in liste
#name: list=[alice ,bob, silviu , davide, marco ]
#print(name)
#min_age: float = float('inf')
#index_min_age: int = 0
#for i in range(len(name)):
#    if name[i].age < min_age:
#        min_age = name[i].age
#        index_min_age = i
#print(name[index_min_age])

# classe animali, rimuovi zampa








class Zoo:
    def __init__(self, fences=[], zookeepers=[]):
        self.fences = fences
        self.zookeepers = zookeepers

        def __str__(self):
            for fence in self.fences:


class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        healt = 100 * (1 / max(age, 1))
        self.health =  healt 


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []  

class Zookeeper: 
    def __init__(self, name: str, surname: str, number: float):
        self.name = name
        self.surname = surname
        self.number = number
    
    def animal_area(self, animal: Animal):
        animal_area = animal.width * animal.height
        return animal_area
    
    def add_animal(self, animal: Animal, fence: Fence):
        animal_area = self.animal_area(animal)  
        if animal not in fence.animals:
            if animal.preferred_habitat == fence.habitat:
                if animal_area <= fence.area:
                    fence.animals.append(animal)
                    fence.area -= animal_area 


    def remove_animal(animal: Animal, fence: Fence):
        animal_area= animal.width * animal.height
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area= fence.area+ animal_area




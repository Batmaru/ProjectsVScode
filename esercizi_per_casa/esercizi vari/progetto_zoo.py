class Zoo:
    def __init__(self, fences=None, zookeepers=None):
        self.fences = fences if fences else []
        self.zookeepers = zookeepers if zookeepers else []
        
    def describe_zoo(self):
        """This function describe the zoo information"""
        description = ""
        if self.zookeepers:
            description += "Guardians:\n"
            for zookeeper in self.zookeepers:
                description += f"{zookeeper}\n"
            description += "#" * 30 + "\n"
        
        if self.fences:
            description += "Fences:\n"
            for fence in self.fences:
                description += f"{fence}\n" + "#" * 30 + "\n"
        
        return description.strip()
        

class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat.lower().capitalize()
        self.health = 100 * (1 / max(age, 1))
        self.fence = None  
        
    def __str__(self) -> str:
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"
    
    
class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat.lower().capitalize()
        self.animals = []  
        
    def __str__(self):
        recinto = f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})\n\nwith animals:\n"
        for animal in self.animals:
            recinto += str(animal) + '\n'
        return recinto.strip()
    
    def feed_animal(self, animal: Animal):
        current_animal_area = animal.height * animal.width
        new_height = animal.height * 1.02
        new_width = animal.width * 1.02
        new_animal_area = new_height * new_width
        required_additional_area = new_animal_area - current_animal_area

        if required_additional_area <= self.area:
            animal.height = new_height
            animal.width = new_width
            animal.health = min(100, animal.health * 1.01)
            self.area -= required_additional_area
            return f"{animal.name} è stato nutrito e ora ha salute {animal.health:.2f} e dimensioni {animal.height:.2f}x{animal.width:.2f}.\n"
        else:
            return "Non c'è abbastanza spazio nel recinto per nutrire l'animale.\n"
    

class ZooKeeper: 
    def __init__(self, name: str, surname: str, id: int):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.id = id
        
    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"
        
    def animal_area(self, animal: Animal):
        return animal.width * animal.height
    
    def add_animal(self, animal: Animal, fence: Fence):
        animal_area = self.animal_area(animal)
        if animal in fence.animals:
            return f"Impossibile aggiungere un animale già presente\n"
        
        if animal.preferred_habitat == fence.habitat:
            if animal_area <= fence.area:
                fence.animals.append(animal)
                fence.area -= animal_area
                animal.fence = fence  
                return f"L'animale {animal.name} è stato aggiunto con successo al recinto.\n"
            else:
                return "Impossibile aggiungere l'animale al recinto, non c'è abbastanza spazio!\n"
        else:
            return "Impossibile aggiungere l'animale al recinto, non rispetta l'habitat!\n"
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += self.animal_area(animal)
            animal.fence = None  
            return f"L'animale {animal.name} è stato rimosso dal recinto.\n"
        else:
            return "L'animale non è presente nel recinto.\n"
    
    def feed(self, animal: Animal):
        if animal.fence:
            return animal.fence.feed_animal(animal)
        return "L'animale non è stato trovato in nessun recinto.\n"
        
    def clean(self, fence: Fence):
        total_occupied_area = sum(self.animal_area(animal) for animal in fence.animals)
        if total_occupied_area == 0:
            return float(fence.area)
        else:
            return total_occupied_area / fence.area

  

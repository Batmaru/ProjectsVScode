class Zoo:
    def __init__(self, fences=[], zookeepers=[]):
        self.fences = fences
        self.zookeepers = zookeepers
        
    def describe_zoo(self):
        """This function describe the zoo information"""
        frase_intera =""
        recinti = ""
        guardiani = ""
        for zookeeper in self.zookeepers:
             guardiani += str(zookeeper) + '\n'
        guardiani+= "\n" + '#' * 30 + '\n'
        frase_intera += (f'Guardians  :\n{guardiani}')
        for fence in self.fences:
            recinti += str(fence) + "\n"+ '#' * 30 + '\n' + '\n'
        frase_intera += (f'Fences:')
        frase_intera += (f'{recinti}')
        return frase_intera

        

class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat.lower().capitalize()
        healt = 100 * (1 / max(age, 1))
        self.health =  healt 
        self.current_fence_animals = []
        self.current_area_remaining= 0
        self.current_fence_area = 0
          # Aggiungi l'attributo current_fence con valore predefinito None
        
    def __str__(self) -> str:
        return f"(name={self.name}, species={self.species}, age={self.age})"
    
    
class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat.lower().capitalize()
        self.animals = []  
        self.remaining = area
        
    def __str__(self):
        recinto=f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})\n\n\n"
        recinto+="with animals:\n"
        for animal in self.animals:
             recinto+= animal.__str__()+ '\n'
        return recinto
    

            
class Zookeeper: 
    def __init__(self, name: str, surname: str, number: float):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.number = number
    
        
    def __str__(self):
        return f'name = {self.name}, surname = {self.surname}, number = {self.number}'
        
    
    #funzione animal_area
    def animal_area(self, animal: Animal):
        animal_area_ = animal.width * animal.height
        return animal_area_
    

    def add_animal(self, animal: Animal, fence: Fence):
        animal_area = self.animal_area(animal)
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.remaining += animal_area
            print("l'animale era gia presente solo che ora ha statistiche diverse da quelle  iniziali perche è stato nutrito")

        animal.current_fence_animals = fence.animals
        animal.current_area_remaining = fence.remaining
        if animal.preferred_habitat == fence.habitat:
            if animal_area <= fence.remaining:
                fence.animals.append(animal)
                fence.remaining -= animal_area
                animal.current_fence_area = fence.area
                animal.current_area_remaining = fence.remaining  
                animal.current_fence_animals=fence.animals  
                return f"L'animale {animal.name} è stato aggiunto o aggiornato con successo al recinto.\n"
            else:
                return "Impossibile aggiungere l'animale al recinto, non c'è abbastanza spazio!.\n"
        else:
            return "Impossibile aggiungere l'animale al recinto, non rispetta l'habitat!.\n"

    
    #funzione remove_animal    
    def remove_animal(self, animal: Animal, fence: Fence):
        animal.current_fence_animals = fence.animals
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.remaining += self.animal_area(animal)
            animal.current_fence_area = fence.area
            animal.current_area_remaining = fence.remaining 
            animal.current_fence_animals=fence.animals  
            return f"L'animale {animal.name} è stato rimosso dal recinto."
        else:
            return "L'animale non è presente nel recinto."
        

    def feed(self, animal: Animal):
        frase_resoconto = ""
        
        area_remaining=animal.current_fence_area

        for animale in animal.current_fence_animals: 
            area_remaining -= self.animal_area(animale)

        animal.current_area_remaining = area_remaining
       
        
        
        if animal in animal.current_fence_animals:
            animal_area = self.animal_area(animal)
            new_health = animal.health + animal.health / 100
            new_height = animal.height + animal.height / 50
            new_width = animal.width +  animal.width / 50
            area_animal_before = self.animal_area(animal)
            food_required = new_height * new_width - animal_area
            if area_remaining > food_required:
                animal.health = new_health
                animal.height = new_height
                animal.width = new_width
                new_area = new_height * new_width
                animal.current_area_remaining -= (new_area - area_animal_before)
                frase_resoconto += f"{animal.name} è stato nutrito. Salute: {new_health}, Altezza : {new_height}, Larghezza : {new_width}\n"
                frase_resoconto += f"Spazio rimanente nel recinto dopo il nutrimento: {animal.current_area_remaining}\n"
                frase_resoconto += f"Spazio  recinto: {animal.current_fence_area}\n"
                frase_resoconto += f"area dell' animale prima del nutrimento: {area_animal_before}\n"
                frase_resoconto += f"area dell' animale dopo il nutrimento: {new_area}\n"
                return frase_resoconto
            else: 
                frase_resoconto += f"animale non nutrito: {animal}, supererebbe l'area disponibile, (area richiesta= {food_required})"   
                return frase_resoconto
        else:
            return  'animale non presente nel recinto'

                
    def clean(self, fence: Fence) :
        area_remaining = fence.area
        for animal in fence.animals:
            area_animal= animal.width * animal.height
            area_remaining-= area_animal 
        
        time = 0.0
        total_occupied_area = fence.area - area_remaining
        
        if total_occupied_area != 0:
            time = total_occupied_area / fence.area
            return time 
        else:
            time = float(fence.area)
            return time


# Creazione di un'istanza di Zookeeper
zookeeper1 = Zookeeper("Mario", "Rossi", 123)

# Creazione di un altra istanza di Zookeeper
zookeeper2 = Zookeeper("Luigi", "Verdi", 456)
     
# Creazione di un'istanza di Fence
savannah = Fence(100, 25, "Savannah")
desert = Fence(80, 30, "Desert")
forest= Fence(70, 30, "forest")        
# Creazione di un'istanza di Zoo con due recinti
zoo2 = Zoo(fences=[savannah, desert, forest], zookeepers=[zookeeper1, zookeeper2])# Creazione di un'istanza di Animal
lion = Animal("Leo", "Lion", 5, 1.2, 2.5, "Savannah")
elephant = Animal("Ellie", "Elephant", 10, 2.5, 5.0, "Savannah")
giraffe = Animal("Gerry", "Giraffe", 7, 4.0, 2.0, "Savannah")
tiger = Animal("Tigro", "Tiger", 6, 1.5, 2.0, "Forest")

# Aggiunta di animali ai recinti
print(zookeeper1.add_animal(lion, savannah))
print(zookeeper1.add_animal(elephant, savannah))
print(zookeeper1.add_animal(giraffe, savannah))
print(zookeeper2.add_animal(tiger, forest))

# Descrizione dello zoo
print(zoo2.describe_zoo())

# Alimentazione degli animali
print(zookeeper1.feed(lion))
print(zookeeper1.add_animal(lion, savannah))
print(zookeeper1.feed(lion))
print(zookeeper1.feed(elephant))
print(zookeeper1.feed(giraffe))
print(zookeeper2.feed(tiger))

# Pulizia dei recinti
print(zookeeper1.clean(savannah))
print(zookeeper1.clean(desert))


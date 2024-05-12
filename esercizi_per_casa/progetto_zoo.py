class Zoo:
    def __init__(self, fences=[], zookeepers=[]):
        self.fences = fences
        self.zookeepers = zookeepers
        
    def describe_zoo(self):
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
    
    #funzione add_animal
    def add_animal(self, animal: Animal):
        animal_area = self.animal_area(animal)
        for fence in zoo.fences:
            if animal not in fence.animals:
                if animal.preferred_habitat == fence.habitat:
                    if animal_area <= fence.remaining:
                        fence.animals.append(animal)
                        fence.remaining -= animal_area 
                        return (f"l'animale: {animal}: è stato aggiunto con successo")
                    
        return(f"l'animale: {animal}: non può essere aggiunto in nessun  recinto")  

    
    #funzione remove_animal    
    def remove_animal(self, animal: Animal):
        for fence in zoo.fences:
            if animal in fence.animals:
                fence.animals.remove(animal)
                fence.remaining += self.animal_area(animal)
                return f"l'animale {animal} e stato  rimosso" + '\n\n'
            else:
                return f"l'animale {animal} non è presente in nessun recinto" + '\n\n'
            
            
               
    def feed_an_animal(self, animal: Animal):
        frase_resoconto = ""
        for fence in zoo.fences:
            if animal in fence.animals:
                animal_area = self.animal_area(animal)
                area_remaining = fence.remaining
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
                    fence.remaining -= (new_area - area_animal_before)
                    frase_resoconto += f"{animal.name} è stato nutrito. Salute: {new_health}, Altezza : {new_height}, Larghezza : {new_width}\n"
                    frase_resoconto += f"Spazio rimanente nel recinto: {fence.remaining}\n"
                    frase_resoconto += f"Spazio  recinto: {fence.area}\n"
                    frase_resoconto += f"area prima del nutrimento: {area_animal_before}\n"
                    frase_resoconto += f'area dopo il nutrimento: {new_area}\n'
        return frase_resoconto + '\n'
        

                            
    def feed(self):
        frase_resoconto = ""
        for fence in zoo.fences:
            for animal in fence.animals:
                resoconto_animale = self.feed_an_animal(animal)
                frase_resoconto += resoconto_animale
        return frase_resoconto

            
    def clean_an_fence(self, fence: Fence) -> str:
        frase_resoconto = ""
        time = 0
        total_occupied_area = fence.area - fence.remaining
        if total_occupied_area != 0:
            time = total_occupied_area / fence.area
            frase_resoconto += f"Dati pulizia del recinto: Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat}\n\n"
            frase_resoconto += f"l'area occupata è di: {total_occupied_area}\n"
            frase_resoconto += f'il tempo richiesto è: {time}\n'
        else:
            time = fence.area
            frase_resoconto += f"Dati pulizia del recinto: Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\n\n"
            frase_resoconto += f"l'area occupata è di: {total_occupied_area}\n"
            frase_resoconto += f'il tempo richiesto è: {time}\n'
        return frase_resoconto + '\n\n'

    
    def clean(self) -> str:
        frase_resoconto = ""
        for fence in zoo.fences:
            frase_resoconto += self.clean_an_fence(fence)
        return frase_resoconto

                            
    
            
# Creazione di un'istanza di Zookeeper
zookeeper1 = Zookeeper("Mario", "Rossi", 123)

# Creazione di un altra istanza di Zookeeper
zookeeper2 = Zookeeper("Luigi", "Verdi", 456)
     
# Creazione di un'istanza di Fence
f = Fence(100, 25, "SavAnnah")

# Creazione di un'istanza di Animal
lion = Animal(name= "Leone", species= "Panthera leo", age=5,height= 2, width=1.0, preferred_habitat="savannah")
tiger = Animal(name= 'tigre', species= 'feline', age = 5, height=2, width=1.0, preferred_habitat= 'Savannah')
giraffe = Animal(name='Giraffe', species='Giraffa', age=6, height=5, width=1.5, preferred_habitat='Savannah')
cheetah = Animal(name='Cheetah', species='Acinonyx', age=4, height=1.5, width=0.8, preferred_habitat='Savannah')
scorpion = Animal(name="Scorpion", species="Scorpiones", age=2, height=0.1, width=0.2, preferred_habitat="Desert")
      
# Creazione di un'istanza di Zoo con due recinti
zoo = Zoo(fences=[f, Fence(80, 30, "Desert"), Fence(70, 30, "forest")], zookeepers=[zookeeper1, zookeeper2])

# Chiamata al metodo add_animal()
zookeeper1.add_animal(lion)
zookeeper1.add_animal(giraffe)
zookeeper1.add_animal(tiger)
zookeeper1.add_animal(cheetah)
zookeeper1.add_animal(scorpion)


zookeeper1.feed()
zookeeper1.clean()

# Creazione di altre istanze di Animal
elephant = Animal(name="Elephant", species="Elephas maximus", age=8, height=3.5, width=2.0, preferred_habitat="forest")
rhinoceros = Animal(name="Rhinoceros", species="Rhinocerotidae", age=6, height=2.2, width=1.2, preferred_habitat="savannah")

# Chiamata al metodo add_animal() del nuovo guardiano dello zoo
zookeeper2.add_animal(elephant)
zookeeper2.add_animal(rhinoceros)

# Chiamata al metodo feed() e clean() del nuovo guardiano dello zoo
zookeeper2.feed()
zookeeper2.clean()

# aggiungiamo un altro animale
cammello = Animal(name="cammello", species="cammello grande", age=8, height=3.5, width=2.0, preferred_habitat="Desert")
zookeeper1.add_animal(cammello)

# Rimuovi un animale che non esiste in un recinto
zookeeper1.remove_animal(Animal(name="NonExistingAnimal", species="Unknown", age=0, height=0, width=0, preferred_habitat="Unknown"))

# Nutri un animale in un recinto pieno
lion_new = Animal(name= "Leone", species= "Panthera leo", age=5,height= 2, width=1.0, preferred_habitat="savannah")
for i in range(5):
    zookeeper1.add_animal(lion_new)
zookeeper1.feed()

# Pulisci un recinto con occupazione nulla
zookeeper1.clean_an_fence(Fence(100, 25, "Desert"))

# Pulisci un recinto con occupazione massima
zookeeper1.clean_an_fence(Fence(100, 25, "Savannah"))

# Aggiungi un altro guardiano allo zoo
zookeeper3 = Zookeeper("Carlo", "Bianchi", 789)
zoo.zookeepers.append(zookeeper3)

# Aggiungi un altro guardiano allo zoo
zookeeper4 = Zookeeper("marwan", "rafik", 256)
zoo.zookeepers.append(zookeeper4)

# Descrivi lo zoo con il nuovo guardiano
print(zoo.describe_zoo())

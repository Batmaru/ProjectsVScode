# Marwan Rafik
# 17/04/2024


print("hello world!")
print("\n")
    
#2.3

#versione breve
name: str = "Mario"
print(f"Ciao {name}")
print("\n")
    
#versione lunga comprehension
message: str = f"ciao {name}, ti va di imparare un pò di python?"
print(message)
print("\n")
    
#2.4
#name, name.upper, name.lower
name_upper=name.upper()
name_lower=name.lower()

print(f"{name}, {name_upper}, {name_lower}")
print("\n")
    
#2.5
phrase: str= "A person who never made a mistake never tried anythingei"
name_p: str= 'Albert Einstein'
print(f'{name_p} una volta disse: "{phrase}"')
print("\n")
    
#2.8
filename: str= "phyton.txt"
print(filename.removesuffix(".txt"))
print("\n")
    
#3.1
name: list = ["marwan", "marco", "silvio", "alberto", "antonio"]
for names in name:
    print(f"{names}")   
print("\n")
    
#3.2
for names in name:
    print(f"ciao, {names}, come stai?")   
print("\n")
    
#3.3
vehicles: list = ["mustang car", "kawasaki motorbike", "caravan", "electric bike", "van"]
for vehicle in vehicles:
    print(f"a {vehicle} would be a great choice")
print("\n")
    
#3.4
guest_list: list = ['Albert Einstein', 'Leonardo da Vinci', 'Marie Curie', 'Nelson Mandela']
for person in guest_list:
    print(f"Dear {person},\nYou are invited to dinner at my place. It would be an honor to have you join us!\nSincerely,\nMarwan")
print("\n")

#3.5
guest_cant_partecipate: list = guest_list.pop(2) 
print(f"unfortunatly {guest_cant_partecipate} can't partecipate\n")

new_guest: str= "Nikola Tesla"
guest_list.insert(2, new_guest)
for person in guest_list:
    print(f"Dear {person},\nYou are invited to dinner at my place. It would be an honor to have you join us!\nSincerely,\nMarwan")
print("\n")

#3.6
print("Good news! We found a bigger dinner table.\n")
guest_list.insert(0, 'Erwin Schrödinger')
guest_list.insert(len(guest_list)//2, 'Werner Karl Heisenberg')
guest_list.append('Niels Bohr')
for person in guest_list:
    print(f"Dear {person},\nYou are invited to dinner at my place. It would be an honor to have you join us!\nSincerely,\nMarwan")
print("\n")

#3.7
print("Unfortunately, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I'm unable to invite you to dinner.")


for person in guest_list:
    print(f"Dear {person},\nYou are still invited to dinner at my place. Please join us!\nSincerely,\nMarwan")
print("\n")

del guest_list[:]
print("List of guests after removing the last two names:", guest_list)

#3.8
places_to_visit: list = ['Japan', 'Italy', 'Australia', 'Canada', 'Brazil']

print("Original order:", places_to_visit)

print("Alphabetical order:", sorted(places_to_visit))

print("Original order after sorted():", places_to_visit)

print("Reverse-alphabetical order:", sorted(places_to_visit, reverse=True))

print("Original order after sorted(reverse=True):", places_to_visit)

places_to_visit.reverse()
print("Reversed order:", places_to_visit)

places_to_visit.reverse()
print("Original order after reversing again:", places_to_visit)

places_to_visit.sort()
print("Sorted order:", places_to_visit)

places_to_visit.sort(reverse=True)
print("Reverse-sorted order:", places_to_visit)
print("\n")

#3.9

guest_list: list = ['Albert Einstein', 'Leonardo da Vinci', 'Nikola Tesla', 'Nelson Mandela']
for person in guest_list:
    print(f"Dear {person},\nYou are invited to dinner at my place. It would be an honor to have you join us!\nSincerely,\nMarwan")
print("\n")

print(f"Number of people invited to dinner: {len(guest_list)}")
print('\n')

#3.10
# Create a list of countries
countries = ['USA', 'Canada', 'France', 'Germany', 'Japan']

# Append: Add a new country to the end of the list
countries.append('Australia')
print("After appending 'Australia':", countries)

# Insert: Add a new country at a specific position
countries.insert(2, 'Brazil')
print("After inserting 'Brazil' at index 2:", countries)

# Remove: Remove a specific country from the list
countries.remove('Germany')
print("After removing 'Germany':", countries)

# Pop: Remove and return the last country from the list
popped_country = countries.pop()
print("Popped country:", popped_country)
print("After popping the last country:", countries)

# Index: Find the index of a specific country in the list
index_france = countries.index('France')
print("Index of 'France':", index_france)

# Count: Count the number of occurrences of a country in the list
count_canada = countries.count('Canada')
print("Count of 'Canada':", count_canada)

# Sort: Sort the list alphabetically
countries.sort()
print("Sorted list of countries:", countries)

# Reverse: Reverse the order of the list
countries.reverse()
print("Reversed list of countries:", countries)

# Clear: Remove all items from the list
countries.clear()
print("After clearing the list:", countries)

#6.1
infoperson: dict = {
    'first_name': 'Marwan', 
    'last_name': 'Rafik', 
    'age': 19, 
    'city': 'Rome'
}

for key, value in infoperson.items():
    print(f'{key.capitalize().replace('_',' ')}: {value}')
print('\n')

#6.2
favorite_numbers: dict = {
    "John": 7,
    "Emily": 22,
    "Michael": 13,
    "Sophia": 8,
    "Daniel": 42}

for key, value in favorite_numbers.items():
    print(f'{key.capitalize().replace('_',' ')}: {value}')
print("\n")

#6.3
glossary: dict = {
    "variable": "A named storage location in memory where data can be stored and retrieved.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A programming construct that repeats a block of code multiple times.",
    "list": "A data structure that holds an ordered collection of items.",
    "dictionary": "A data structure that stores key-value pairs."
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(meaning)
    print('\n')

# 6.7
person1: dict = {
    'first_name': 'Marwan', 
    'last_name': 'Rafik', 
    'age': 19, 
    'city': 'Rome'
 }


person2: dict= {
    "first_name": "Emily",
    "last_name": "Smith",
    "age": 25,
    "city": "Los Angeles"
}

person3: dict= {
    "first_name": "Michael",
    "last_name": "Johnson",
    "age": 40,
    "city": "Chicago"
}

people: list = [person1, person2, person3]


for person in people:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print('\n') 


#6.8
pet1: dict= {
    "kind": "Dog",
    "owner": "Alice"
}

pet2: dict= {
    "kind": "Cat",
    "owner": "Bob"
}

pet3: dict= {
    "kind": "Parrot",
    "owner": "Charlie"
}

pets: list = [pet1, pet2, pet3]

for pet in pets:
    print("Kind of Animal:", pet["kind"])
    print("Owner's Name:", pet["owner"])
    print('\n')

#6.9
favorite_places: dict = {
    "Alice": ["Paris", "Kyoto"],
    "Bob": ["New York"],
    "Charlie": ["Sydney", "London", "Rome"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f'-{place}')
    print()  
    
#6.10
favorite_numbers: dict = {
    "John": [7, 11, 23],
    "Emily": [22, 8],
    "Michael": [13, 17, 19],
    "Sophia": [8, 42],
    "Daniel": [42, 3, 9]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    num_numbers = len(numbers) 
    for index in range(num_numbers):
        number = numbers[index]
        if index < num_numbers - 1:
            print(f"{number},", end=" ")
        else:
            print(number)
    print() 

#6.11
cities: dict = {
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "New York": {
        "country": "United States",
        "population": 8336697,
        "fact": "New York City is known as the 'Big Apple'."
    },
    "London": {
        "country": "United Kingdom",
        "population": 8908081,
        "fact": "London's Underground is the oldest underground railway network in the world."
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()  


#6.12
cities: dict = {
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "area": 2187,  # in square kilometers
        "landmarks": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing"],
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "New York": {
        "country": "United States",
        "population": 8336697,
        "area": 783.8,
        "landmarks": ["Statue of Liberty", "Empire State Building", "Central Park"],
        "fact": "New York City is known as the 'Big Apple'."
    },
    "London": {
        "country": "United Kingdom",
        "population": 8908081,
        "area": 1572, 
        "landmarks": ["Big Ben", "Tower Bridge", "Buckingham Palace"],
        "fact": "London's Underground is the oldest underground railway network in the world."
    }
}


for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")  
    print(f"Area: {info['area']} square kilometers")  
    print("Landmarks:", ", ".join(info['landmarks']))  
    print(f"Fact: {info['fact']}")
    print()  
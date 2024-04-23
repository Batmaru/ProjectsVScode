#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use 
#a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the 
#pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output 
#should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as#
#I really love pizza!

pizzas: list[str] = ['margherita', 'bufala', 'pachino']
print('my favorites pizzas are:')
for pizza in pizzas:
    print(f'{pizza}')
print()


def favorite_pizza(pizza_list):
    print(f'my favorites pizzas are: {pizza_list}')
    for pizza in (pizza_list):
        print(f'i like {pizza}')
    

favorite_pizza(pizzas)
print("\n")
favorite_pizza(pizzas)
print('I really love pizza!')

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a 
#sentence, such as Any of these animals would make a great pet!

animals: list[str]= ['tiger', 'lion', 'cat']

for animal in animals:
    print(animal)
print()

for animal in animals:
    print(f'A {animal}, is an animal.')
print()

for animal in animals:
    print(f'A {animal}, is an animal.')
print('These animals are feline.')
print()

#4.3
N: list[float]= []
for n in range(1, 21):
    N.append(n)
print(N)
print()

#4.4
N1: list[float]= []
for n in range(1000001):
    N1.append(n)
#print(N1)
print()

#4.5
N2: list[float]= []
for n in range(1, 1000001):
    N2.append(n)
max_value=max(N2)
min_value=min(N2)
print('maximum value=', max_value)
print('minimum value=', min_value)
print()

#4.6
l1: list[float]=[]
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    l1.append(number)
print(l1)
print()

#4.7
multiple_of_3: list[float]=[]
for m in range(3,31,3):
    multiple_of_3.append(m)
print('I multipli di 3 sono:', multiple_of_3)
print()

#4.8
import time

start: float = time.time()
nel4: list[float] = []
for n in range(0,10001):
    n= n**3
    nel4.append(n)
print(f"Il tempo impiegato è {time.time() - start}")

#print(nel4)
print()

#4.9
start: float = time.time()
mylist: list=[n**3 for n in range(10000)]
print(f"Il tempo impiegato è {time.time() - start}")
#print(mylist)
print()


my_list: list = [1, 2, 3, 4, 5, 6, 7, 8]
prime_tre_item: list = my_list[:3]
indice_centrale: int = len(my_list) // 2
indice_precedente: int = indice_centrale - 1
elementi_centrali: list = my_list[indice_precedente: indice_centrale + 1]
ultimi_tre_item: list = my_list[-3:]

nuova_list: list = [prime_tre_item, elementi_centrali, ultimi_tre_item]


#4.10
nel3=[]
for n in range(0,101):
    nel3.append(n)
nel3_slice = []
primi_tre_numeri: list = nel3[:3]
nel3_slice.extend(primi_tre_numeri)
if len(nel3)%2==0:
    print('la lista è pari:')
    nel3_slice = []
    primi_tre_numeri: list = nel3[:3]
    nel3_slice.extend(primi_tre_numeri)
    indice_mezzo= len(nel3)//2
    indice_mezzo_sin= indice_mezzo-1
    indice_mezzo_dest=indice_mezzo_sin+1
    due_numeri_mezzo: list = [nel3[indice_mezzo_sin], nel3[indice_mezzo_dest]]
    nel3_slice.extend(due_numeri_mezzo)
    nel3_slice.extend(nel3[-3:])
    print(nel3_slice)
else:
    print('la lista è dispari')
    nel3_slice = []
    primi_tre_numeri: list = nel3[:3]
    nel3_slice.extend(primi_tre_numeri)
    indice_mezzo_muno= len(nel3)//2
    indice_mezzo=indice_mezzo_muno
    indice_mezzo_meno1= indice_mezzo-1
    indice_mezzo_piu1= indice_mezzo+1
    tre_numeri_mezzo: list = [nel3[indice_mezzo_meno1], nel3[indice_mezzo], nel3[indice_mezzo_piu1]]
    nel3_slice.extend(tre_numeri_mezzo)
    nel3_slice.extend(nel3[-3:])
    print(nel3_slice)
print()

#4.11
#My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call 
#it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then 
# use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'

friends_pizza: list[str]=[]
for pizza in pizzas:
    friends_pizza.append(pizza)
pizzas.append('4 formaggi')
friends_pizza.append('rossa')
print('my favorite pizzas are:', pizzas,'\n')
print("my friend's favorite pizzas are:", friends_pizza,'\n')

#4-12. 
# More Loops: All versions of foods.py in this section have avoided using for loops when printing, 
# to save space. Choose a version of foods.py, and write two for loops to print each list of foods.


# Lista di cibi
my_foods = ['pizza', 'chicken', 'chocolate cake']
friend_foods = my_foods[:]
friend_foods.append('icecream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
print()

#4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/. 
# You won’t use much of it now, but it might be interesting to skim through it.





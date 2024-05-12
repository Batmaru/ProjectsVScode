class Food:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self) -> str:
        if self.description:
            return f'{self.name.capitalize()}(price={self.price},descr={self.description})'
        else:
            return f'{self.name.capitalize()}(price={self.price})'

class Menu:
    def __init__(self, foods = [] ):
        self.foods = foods
       
    def addFood(self, food):
       self.foods.append(food)
    
    def removeFood(self, food):
        self.foods.remove(food)

    def __str__(self)->str:
        repr: str =""
        for food in self.foods:
            repr += f'{food}\n'
        return repr
    
    def printPrices(self):
        for food in self.foods:
            print(food.name, food.price, food.description)
    
    def getAveragePrice(self):
        if not self.foods:
            return 0
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)
    

food1= Food(name='pizza margherita', price=6, description='pizza margherita is cool')
food2= Food(name='pasta al ragù', price= 8, description=' pasta al ragù s cool')
food3= Food(name='cono gelato', price= 3, description='cono is cool')

menu = Menu()


menu.addFood(food1)
menu.addFood(food2)
menu.addFood(food3)

food4 = Food("lasagna", 12,'lasagna is cool')
food5 = Food("Sushi", 15, 'sushi is cool')
menu.addFood(food4)
menu.addFood(food5)

print(menu.__str__())

average_price = menu.getAveragePrice()
print(f"Average price of items on the menu: ${average_price}")




    


    
    
        




 
# 1. Create a class called Shape with an abstract method called area and another abstract method called
# perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter method.
# 2. Create a class called Shape with an abstract method called area and another abstract method called
# perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter method.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
cerchio1= Circle(radius=10)
print(cerchio1.area())
        
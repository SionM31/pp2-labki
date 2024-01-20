"""
 Define a class named Rectangle which inherits from Shape class from task 2.

 Class instance can be constructed by a length and width.
 
 The Rectangle class has a method which can compute the area.
"""

from ex_2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
    
    def get_area(self):
        self.area = self.length * self.width
        print(f'The area is: {self.area}')


x = Rectangle(2, 3)
x.get_area()
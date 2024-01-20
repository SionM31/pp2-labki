"""
 Define a class named Shape and its subclass Square.
 
 The Square class has an init function which takes a length as argument.
 
 Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    def __init__(self):
        self.area = 0
    
    def get_area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        self.length = int(length)
        self.area = self.length * self.length
    
    def get_area(self):
        print(f'The area of the square is equal to: {self.area}')



#x = Square(2)
#x.get_area()
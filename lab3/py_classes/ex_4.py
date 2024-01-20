"""
 Write the definition of a Point class. Objects from this class should have a
 
  a method show to display the coordinates of the point
  
  a method move to change these coordinates
  
  a method dist that computes the distance between 2 points
"""
from math import *

class Point:
    def __init__(self):
        self.x = 0 # default x
        self.y = 0 # default y
    
    def show(self):
        print(f'x: {self.x}, y: {self.y}')
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, comp_x, comp_y):
        dx = self.x - comp_x
        dy = self.y - comp_y
        distance = sqrt(dx * dx + dy * dy)
        print(f'The distance is: {distance}')


x = Point()
x.show()
x.move(1, 1)
x.show()
x.dist(0, 0)
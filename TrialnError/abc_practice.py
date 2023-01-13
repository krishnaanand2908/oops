from abc import ABC, abstractclassmethod

class Parallelogram(ABC):
    @abstractclassmethod
    def areaofshape(self, base, height):
        return self.base * self.window_height

class Rectangle():
    def __init__(self, length, breadth):
        self.base = length
        self.height = breadth
    def areaofshape(self, base, height):
        base = self.base
        height = self.height
        return base * height
              
              
abcd = Rectangle(10, 15)
print(abcd.areaofshape(10, 15))
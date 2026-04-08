'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 10 Assignemt 4
'''

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

    def display_info(self):
        return f"Shape: {self.name}"
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def display_info(self):
        return f"{super().display_info()}, Radius: {self.radius}, Area: {self.area():.2f}"
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def display_info(self):
        return f"{super().display_info()}, Radius: {self.radius}, Area: {self.area():.2f}"
    
    @classmethod
    def create_circle(cls, radius):
        try:
            radius = float(radius)
            if radius <= 0:
                raise ValueError("Radius must be greater than 0.")
            return cls(radius)
        except ValueError as e:
            print(f"Could not create circle: {e}")
            return None
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def display_info(self):
        return (
            f"{super().display_info()}, Length: {self.length}, Width: {self.width},"
             f"Area: {self.area():.2f}"
        
        )
    
    @classmethod
    def create_rectangle(cls, length, width):
        try:
            length = float(length)
            width = float(width)
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be greater than 0.")
            return cls(length, width)
        except ValueError as e:
            print(f"Could not create rectangle: {e}")
            return None
    
def run_demo():
    try:
        circle = Circle.create_circle(7)
        rectangle = Rectangle.create_rectangle(10, 4)

        if circle:
            print(circle.display_info())
        if rectangle:
            print(rectangle.display_info())

        print ('\n') 
        print('==========Attempting to create shapes with invalid dimensions==========')
        Circle.create_circle(-3)
        Rectangle.create_rectangle("long", 5)
    except Exception as error:
        print(f"Unexpected error in shapes demo: {error}")

if __name__ == "__main__":
    run_demo()
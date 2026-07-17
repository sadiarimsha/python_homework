import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

point1 = Point(2, 4)
point2 = Point(3, 5)

print(point1 == point2)
print(point1.distance_to(point2))
print(point1)
print(point2)


vector1 = Vector(4, 8)
vector2 = Vector(5, 9)

print(vector1 == vector2)
print(vector1.distance_to(vector2))
print(vector1 + vector2)

print(vector1)
print(vector2)
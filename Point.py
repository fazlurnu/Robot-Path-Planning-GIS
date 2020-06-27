from math import *

class Point:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def distance(self, other):
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]

        return sqrt(dx**2 + dy**2)
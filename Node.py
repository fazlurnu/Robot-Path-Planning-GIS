from math import *

# This class represent a node
class Node:

    # Initialize the class
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f

    def distance(self, other):
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]

        return sqrt(dx**2 + dy**2)
    # Print node
    #def __repr__(self):
    #    return ('({0},{1})'.format(self.position, self.f))
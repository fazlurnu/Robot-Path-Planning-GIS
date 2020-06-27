from Node import Node
from Robot import Robot
from Display import Display
from Graph import Graph

import math
import random

# The main entry point for this module
def main():

    nodes = []
    pos = [(100, 400), (350, 300), (350, 560), (500, 350), (500, 550), (650, 350)]
    
    for i, po in enumerate(pos):
        name = str(i)
        nodes.append(Node(po, name))

    #nodes = []
    #for i in range(6):
    #    x = random.randint(50, 700)
    #    y = random.randint(50, 700)
    #    position = (x,y)
    #    name = str(i)
    #    nodes.append(Node(position, name))

    start = nodes[0].position
    end = nodes[len(nodes)-1].position

    edges = [(nodes[0], nodes[1]), (nodes[0], nodes[2]), (nodes[1], nodes[3]), (nodes[2], nodes[3]),
             (nodes[2], nodes[4]), (nodes[3], nodes[5]), (nodes[4], nodes[5])]

    graph = Graph()

    graph.connect(nodes[0].name, nodes[1].name, nodes[0].distance(nodes[1]))
    graph.connect(nodes[0].name, nodes[2].name, nodes[0].distance(nodes[2]))
    graph.connect(nodes[1].name, nodes[3].name, nodes[1].distance(nodes[3]))
    graph.connect(nodes[2].name, nodes[3].name, nodes[2].distance(nodes[3]))
    graph.connect(nodes[2].name, nodes[4].name, nodes[2].distance(nodes[4]))
    graph.connect(nodes[3].name, nodes[5].name, nodes[3].distance(nodes[5]))
    graph.connect(nodes[4].name, nodes[5].name, nodes[4].distance(nodes[5]))

    print(graph.nodes())

    
    robot = Robot(position = [start[0],start[1]], heading = math.pi)

    route = [nodes[0], nodes[1], nodes[3], nodes[5]]

    display = Display(robot, nodes, edges, route)

# Tell python to run main method
if __name__ == "__main__":
    main()
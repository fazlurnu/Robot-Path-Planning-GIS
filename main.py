from astar import astar_search
from Node import Node
from Point import Point
from Robot import Robot
from Display import Display
from Graph import Graph

import math
import random

# The main entry point for this module
def main():

    # uncomment below to define coordinates
    #pos = [(100, 400), (350, 100), (350, 560), (500, 100), (500, 550), (650, 400)]
    
    # randomize coordinate
    nb_of_nodes = 30
    pos = []
    for i in range(nb_of_nodes):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        pos.append((x,y))

    # create list of coordinate inside nodes
    nodes = []
    for i, po in enumerate(pos):
        name = str(i)
        nodes.append(Point(name, po))

    start = nodes[0]
    end = nodes[len(nodes)-1]

    # uncomment below to define edges (connection between nodes)
    #edges = [(nodes[0], nodes[1]), (nodes[0], nodes[2]), (nodes[1], nodes[3]), (nodes[1], nodes[4]),
    #         (nodes[2], nodes[3]), (nodes[2], nodes[4]), (nodes[3], nodes[5]), (nodes[4], nodes[5])]

    #create edges randomly
    p = 0.3
    edges = []
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if (random.uniform(0,5)<p):
                edges.append((nodes[i], nodes[j]))

    #create graph
    graph = Graph()

    for edge in edges:
        graph.connect(edge[0].name, edge[1].name, edge[0].distance(edge[1]))

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    for node in nodes:
        heuristics[node.name] = node.distance(end)

    # Run the search algorithm
    path = astar_search(graph, heuristics, start.name, end.name)

    robot = Robot(position = [start.position[0],start.position[1]], heading = math.pi)
    
    if path is not None:

        route = []
        for node in path:
            index = int(node)
            route.append(nodes[index])    

        display = Display(robot, nodes, edges, route)
    else:
        print("Can't find route")

# Tell python to run main method
if __name__ == "__main__":
    main()
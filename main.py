from Node import Node
from Robot import Robot
from Display import Display

import math

# The main entry point for this module
def main():

    start = (200, 300)
    end = (800, 750)
    pos1 = (500, 400)
    pos2 = (300, 600)

    nodes = []
    nodes.append(Node(start))
    nodes.append(Node(pos1))
    nodes.append(Node(pos2))
    nodes.append(Node(end))

    edges = [(nodes[0], nodes[1]), (nodes[1], nodes[2]), (nodes[2], nodes[3])]
    robot = Robot(position = [start[0],start[1]], heading = math.pi)

    display = Display(robot, nodes, edges)

# Tell python to run main method
if __name__ == "__main__":
    main()
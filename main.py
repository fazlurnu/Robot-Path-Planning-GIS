from Node import Node
from Robot import Robot
from Display import Display

import math

# The main entry point for this module
def main():

    nodes = []
    for i in range(4):
        for j in range(4):
            position = (i,j)
            nodes.append(Node(position))

    robot = Robot((50,50))
    display = Display(robot)

# Tell python to run main method
if __name__ == "__main__":
    main()
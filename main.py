from Node import Node
from Robot import Robot
from Display import Display

import math

# The main entry point for this module
def main():

    start = (200, 300)
    end = (800, 750)

    nodes = []
    nodes.append(Node(start))
    nodes.append(Node(end))

    robot = Robot(position = [start[0],start[1]], heading = 0)
    robot.set_goal(end)

    display = Display(robot, nodes)

# Tell python to run main method
if __name__ == "__main__":
    main()
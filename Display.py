from Robot import Robot
import pygame

from math import *

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255, 0, 0)
GREEN=(0,255,0)
BLUE=(0,0,255)

FRAMES_PER_SECOND = 30

class Display:

    def __init__(self, robot, nodes):

        self.height = 1000
        self.width = 1000

        caption = 'Python Code for Robot Command'
        pygame.init()
        print("Initialize PyGame Display, Caption: " + caption + ", size: " + str(self.width) + "x" + str(self.height))
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screen.fill(WHITE)

        border_width = 5

        self.display(robot, nodes)

    def draw_robot(self, robot):
        radius = 20
        pos_x = int(robot.position[0])
        pos_y = int(robot.position[1])
        
        start_line_x = pos_x
        start_line_y = pos_y
        end_line_x = pos_x + radius * cos(robot.heading)
        end_line_y = pos_y + radius * sin(robot.heading)

        pygame.draw.circle(self.screen, RED, (pos_x, pos_y), radius)

        pygame.draw.line(self.screen, BLACK, (start_line_x, start_line_y), (end_line_x, end_line_y), 5)

    def draw_nodes(self, nodes):
        for node in nodes:
            pygame.draw.circle(self.screen, GREEN, node.position, 10)

    def display(self, robot, nodes):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    sys.exit()

            velo = 1
            
            if not robot.is_directed():
                robot.rotate(0.1)
            else:
                if (robot.is_at_goal()):
                    robot.translate(0)
                else:
                    print(robot.distance_to_goal())
                    robot.translate(2)

            self.screen.fill(WHITE)
            self.draw_nodes(nodes)
            self.draw_robot(robot)

            #clock.tick(FRAMES_PER_SECOND)
            
            pygame.display.update()

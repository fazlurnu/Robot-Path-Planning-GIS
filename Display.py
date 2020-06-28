from Robot import Robot
import pygame

from math import *

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255, 0, 0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW = (255, 255, 0)

FRAMES_PER_SECOND = 30

class Display:

    def __init__(self, robot, nodes, edges, route):

        self.height = 1000
        self.width = 1000

        caption = 'Python Code for Robot Command'
        pygame.init()
        
        self.font = pygame.font.Font('FreeSansBold.ttf', 20)

        print("Initialize PyGame Display, Caption: " + caption + ", size: " + str(self.width) + "x" + str(self.height))
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screen.fill(WHITE)

        border_width = 5

        self.display(robot, nodes, edges, route)

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
            
            if (node.name == '0'):
                color = YELLOW
            elif (node.name == str(len(nodes)-1)):
                color = RED
            else:
                color = GREEN

            pygame.draw.circle(self.screen, color, node.position, 15)
            text = self.font.render(node.name, True, BLACK, color)
            textRect = text.get_rect()  
            textRect.center = node.position

            self.screen.blit(text, textRect) 

    def draw_edges(self, edges):
        for edge in edges:
            pygame.draw.line(self.screen, BLACK, edge[0].position, edge[1].position, 5)

    def draw_route(self, nodes, route):
        for i in range(len(route)-1):
            start_index = int(route[i].name)
            end_index = int(route[i+1].name)
            start = nodes[start_index]
            end = nodes[end_index]
            pygame.draw.line(self.screen, RED, start.position, end.position, 5)

    def display(self, robot, nodes, edges, route):
        
        #waypoint following initialization
        node_reached = 0
        total_target = len(route)-1

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    done = True
                    pygame.quit()
                    sys.exit()

            # robot control
            robot.set_goal(route[node_reached+1].position)

            if not robot.is_directed():
                # set rotation speed
                robot.rotate(0.05)
                #print(robot.heading)
            else:
                if (robot.is_at_goal()):
                    # stop when goal is reached
                    # set robot speed equals to 0
                    robot.translate(0)

                    # go to next node
                    node_reached+=1
                else:
                    # set robot speed equals to 2
                    robot.translate(2)

            if (node_reached==total_target):
                done = True

            # end of robot control

            #visualization

            self.screen.fill(WHITE)
            self.draw_edges(edges)
            self.draw_route(nodes, route)
            self.draw_nodes(nodes)
            self.draw_robot(robot)

            #end of visualization
            
            pygame.display.update()

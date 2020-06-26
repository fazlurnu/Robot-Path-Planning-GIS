# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:53:41 2020

@author: My Laptop
"""

from Node import Node
from astar import astar

import pygame, sys
from pygame.locals import *

class Grid:
    
    def __init__(self, coordinates, start, end, edges):
        
        row = 10
        col = 10

        self.width = 50
        self.height = 50
        
        pygame.init()
        pygame.display.set_caption('Python Code for Robot Command')
        self.screen = pygame.display.set_mode((row * self.width, col * self.height))
        
        pygame.init()


        WHITE=(255,255,255)
        TOSCA=(0, 200, 200)
        BLACK=(0,0,0)
        RED=(255, 0, 0)
        GREEN=(0,255,0)
        BLUE=(0,0,255)
        self.screen.fill(WHITE)


        for edge in edges:
            start_node = edge[0]
            end_node = edge[1]

            start_point_y = int(start_node[0]*self.width + self.width/2)
            start_point_x = int(start_node[1]*self.height + self.height/2)
            
            end_point_y = int(end_node[0]*self.width + self.width/2)
            end_point_x = int(end_node[1]*self.height + self.height/2)

            pygame.draw.line(self.screen, BLACK, (start_point_x, start_point_y), 
                            (end_point_x, end_point_y), 3)

        for coordinate in coordinates:
           point_y = int(coordinate[0]*self.width + self.width/2)
           point_x = int(coordinate[1]*self.height + self.height/2)

           pygame.draw.circle(self.screen, GREEN, [point_x, point_y], 5) 

        start_point_y = int(start[0]*self.width + self.width/2)
        start_point_x = int(start[1]*self.height + self.height/2)

        pygame.draw.circle(self.screen, BLUE, [start_point_x, start_point_y], 5)

        end_point_y = int(end[0]*self.width + self.width/2)
        end_point_x = int(end[1]*self.height + self.height/2)

        pygame.draw.circle(self.screen, RED, [end_point_x, end_point_y], 5)

        """for i in range (1, len(paths)):
           start_point_y = int(paths[i-1][0]*self.width + self.width/2)
           start_point_x = int(paths[i-1][1]*self.height + self.height/2)
            
           end_point_y = int(paths[i][0]*self.width + self.width/2)
           end_point_x = int(paths[i][1]*self.height + self.height/2)
           
           #pygame.draw.line(self.screen, RED, (start_point_x, start_point_y), 
                            #(end_point_x, end_point_y), 10)
            
        pygame.draw.circle(self.screen, GREEN, [start_point_x, start_point_y], 5) 
        """
        
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        
        
        
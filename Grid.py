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
    
    def __init__(self, maze, paths):
        self.cols = len(maze)
        self.rows = len(maze[0])
        
        print("Hello from grid, " + str(self.rows) + "x" + str(self.cols))
    
        self.width = 100
        self.height = 100
        
        pygame.init()
        pygame.display.set_caption('Python Code for Robot Command')
        self.screen = pygame.display.set_mode((self.cols * self.width, self.rows * self.height))
        
        pygame.init()


        WHITE=(255,255,255)
        TOSCA=(0, 200, 200)
        BLACK=(0,0,0)
        RED=(255, 0, 0)
        GREEN=(0,255,0)
        self.screen.fill(WHITE)

        border_width = 5
        
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if (cell):
                    pygame.draw.rect(self.screen,BLACK,(j*self.width + border_width, i*self.height + border_width, self.width - border_width,self.height - border_width))
                else:
                    pygame.draw.rect(self.screen,TOSCA,(j*self.width + border_width, i*self.height + border_width, self.width - border_width,self.height - border_width))
                    
        for i in range (1, len(paths)):
           start_point_y = int(paths[i-1][0]*self.width + self.width/2)
           start_point_x = int(paths[i-1][1]*self.height + self.height/2)
            
           end_point_y = int(paths[i][0]*self.width + self.width/2)
           end_point_x = int(paths[i][1]*self.height + self.height/2)
           
           pygame.draw.line(self.screen, RED, (start_point_x, start_point_y), 
                            (end_point_x, end_point_y), 10)
           
           if (i==1):
               pygame.draw.circle(self.screen, GREEN, [start_point_x, start_point_y], 20)
               
           if (i==len(paths)-1):
               pygame.draw.circle(self.screen, RED, [end_point_x, end_point_y], 20)
                       
        
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:37:10 2020

@author: My Laptop
"""
#from astar import astar
from Grid import Grid
import random

def main():

    nodes = []

    for i in range(10):
        for j in range(10):
            
            node = (i,j)
            nodes.append(node)

    #print(coordinates)

    start = nodes[0]
    end = nodes[len(nodes)-1]

    
    edges = []

    for i in range(10):
        for j in range(9):
            edge = [nodes[i*10+j], nodes[i*10+j+1]]
            edges.append(edge)

    for i in range(1, 10):
        for j in range(10):
            index = i*10+j
            edge = [nodes[index], nodes[index-10]]
            edges.append(edge)

    print(edges)
    
    #path = astar(maze, start, end)
    
    #print(path)
    grid = Grid(nodes, start, end, edges)


if __name__ == '__main__':
    main()
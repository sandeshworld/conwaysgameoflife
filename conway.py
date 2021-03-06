"""
Conway's Game of Life Backend-End
Written by Sandesh Banskota as a simple & fun side project.
11/28/2020
"""

import numpy as np
import random
import time
import copy

class World:

    # initialize backend world to run the simulation on
    def __init__(self,matrix,size):
        #for now 2d list but array for larger set in the future
        self.dimension = size
        self.earth = matrix
        self.iteration = 0
        
        self.neighbor_count = copy.deepcopy(self.earth) # useful for debugging neighbor count


    #  defines rules for conway's game of life
    def _worst_runtime_rules(self):        
        index_range = range(self.dimension)
        #print("Earth")
        #print(self.earth)
        new_world = copy.deepcopy(self.earth) #fixed array copying bug
        for row in index_range:
            for column in index_range:
                num_of_neighbors = self._check_neighbors(row,column)
                # self.neighbor_count[row][column] = num_of_neighbors
                if self.earth[row][column] != 0:
                    if (num_of_neighbors < 2) or (num_of_neighbors > 3):
                        new_world[row][column] = 0
                else:
                    if num_of_neighbors == 3:
                        new_world[row][column] = 1

        self.earth = copy.deepcopy(new_world)
        self.iteration += 1

    # function to check the number of alive neighbors per given cell location
    # return int of how many neighbors are alive
    def _check_neighbors(self, x, y): 
        alive_neighbors = 0
        # handle edge cases using try and except
        # automate instead of writing every neighbor case
        options = [1,0,-1]
        for dx in options:
            for dy in options:
                try:
                    if not (dx == 0 and dy == 0): # make sure that it doesn't count x,y (itself) as a neighbor 
                        if self.earth[x+dx][y+dy] != 0:
                            alive_neighbors += 1
                except:
                    do_nothing = 0            
        return alive_neighbors


    # function called to run iteration on the game of life world
    def run_interation(self):
        self._worst_runtime_rules()
        return self.earth
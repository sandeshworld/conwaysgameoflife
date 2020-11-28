import numpy as np
import random
import time
import copy
from game_gui import SimulationGUI

class World:

    def __init__(self,size=10,seed=random.randint(0,10)):
        #for now 2d list but array for larger set in the future
        self.dimension = size
        self.earth = np.zeros((size,size))
        self.iteration = 0
        
        self.neighbor_count = copy.deepcopy(self.earth) # useful for debugging neighbor count

        #test seeds
        self.earth[5,5] = 1
        self.earth[6,5] = 1
        self.earth[7,5] = 1
        # self.earth[4,4] = 1
        # self.earth[4,6] = 1
        # self.earth[4,3] = 1

        # self.earth[49,50] = 1
        # self.earth[51,51] = 1
        # self.earth[52,52] = 1
        # self.earth[51,53] = 1
    

    #  defines rules for conway's game of life
    def worst_runtime_rules(self):        
        index_range = range(self.dimension)
        print("Earth")
        print(self.earth)

        new_world = copy.deepcopy(self.earth) #fixed array copying bug

        for row in index_range:
            for column in index_range:
                num_of_neighbors = self._check_neighbors(row,column)
                self.neighbor_count[row][column] = num_of_neighbors
                if self.earth[row][column] != 0:
                    if (num_of_neighbors < 2) or (num_of_neighbors > 3):
                        new_world[row][column] = 0
                else:
                    if num_of_neighbors == 3:
                        new_world[row][column] = 1

        self.earth = copy.deepcopy(new_world)
        self.iteration += 1

    # more so a private function to check neighbors used often
    def _check_neighbors(self, x, y):
        # return int of how many neighbors are alive
        
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


    # got stuck using matplotlib animation... use tkinter instead
    def start_sim(self,iterations=100):
        # initializing    
        for i in range(iterations):
            self.worst_runtime_rules()
            # print("Earth")
            # print(self.earth) # posts earth after modified so doesn't correspond with neighbor count array
            print("Neighbor Count")
            print(self.neighbor_count)
            time.sleep(1)
        




def main():
    world = World()
    gui = SimulationGUI() # testing ... it works
    world.start_sim()





if __name__ == "__main__":
    main()




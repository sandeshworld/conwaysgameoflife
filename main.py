import numpy as np
import random
import time

class World:

    def __init__(self,size=100,seed=random.randint(0,10)):
        #for now 2d list but array for larger set in the future
        self.dimension = size
        self.earth = np.zeros((size,size))
        self.iteration = 0
        
        #test seeds
        self.earth[50,50] = 1
        self.earth[50,51] = 1
        self.earth[49,50] = 1
        self.earth[51,51] = 1
        self.earth[52,52] = 1
        self.earth[51,53] = 1
    

    def worst_runtime_rules(self):
        
        index_range = range(self.dimension)
        
        new_world = self.earth

        for row in index_range:
            for column in index_range:
                if self.earth[row][column] != 0:
                    if (self.check_neighbors(row,column) < 2) or (self.check_neighbors(row,column) > 3):
                        new_world[row][column] = 0
                else:
                    if self.check_neighbors(row,column) == 3:
                        new_world[row][column] = 1

        self.earth = new_world
        self.iteration += 1


    #probably a bad implementation
    def check_neighbors(self, x, y):
        #return int of how many neighbors are alive
        
        if x == 0 and y == 0:
            neighbor_coordinates = [self.earth[x+1][y], self.earth[x][y+1], 
                                self.earth[x+1][y+1]]
        if x == 0 and y == self.size-1:
            neighbor_coordinates = [self.earth[x+1][y], self.earth[x][y+1], 
                                self.earth[x][y-1]]        
        
        alive_neighbors = 0 

        for i in neighbor_coordinates:
            if i != 0:
                alive_neighbors += 1
        
        return alive_neighbors

            

    def start_sim(self,iterations=100):
        for i in range(iterations):
            self.worst_runtime_rules()
            print(self.earth)
            time.sleep(1)

def main():
    world = World()
    world.start_sim()



if __name__ == "__main__":
    main()




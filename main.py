import numpy as np
import random
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation

class World:

    def __init__(self,size=10,seed=random.randint(0,10)):
        #for now 2d list but array for larger set in the future
        self.dimension = size
        self.earth = np.zeros((size,size))
        self.iteration = 0
        
        #test seeds
        self.earth[5,5] = 1
        self.earth[5,6] = 1
        self.earth[6,5] = 1
        self.earth[4,5] = 1

        # self.earth[49,50] = 1
        # self.earth[51,51] = 1
        # self.earth[52,52] = 1
        # self.earth[51,53] = 1
    

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

    # probably a bad implementation
    def check_neighbors(self, x, y):
        # return int of how many neighbors are alive
        
        alive_neighbors = 0
        # handle edge cases using try and except
        # automate instead of writing every neighbor case
        options = [1,0,-1]
        for dx in options:
            for dy in options:
                try:
                    if x != 0 and y != 0:
                        if self.earth[x+dx][y+dy] != 0:
                            alive_neighbors += 1
                except:
                    do_nothing = 0            
        
        return alive_neighbors


    # got stuck using matplotlib animation... use tkinter instead
    def start_sim(self,iterations=100):
        # initializing
        fig = plt.figure()
        
        image = list(self.earth)

        new_image = []
        for i in range(len(image)):
            new_image.append([])
            for k in range(len(image[i])):
                if image[i][k] == 0:
                    new_image[i].append([0, 0, 0])
                else:
                    new_image[i].append([255,255,255])
        
        im = plt.imshow(new_image)

        def iter_function(i):
            self.worst_runtime_rules()

            image = list(self.earth)

            new_image = []
            for i in range(len(image)):
                new_image.append([])
                for k in range(len(image[i])):
                    if image[i][k] == 0:
                        new_image[i].append([0, 0, 0])
                    else:
                        new_image[i].append([255,255,255])
            
            im.set_data(new_image)
            return im


            # imgplot = plt.imshow(image)
            # plt.show()
            # plt.close()
            # time.sleep(0.5)
        plt.show()
        anim = animation.FuncAnimation(fig,iter_function, frames=5 * 5, interval=50)
        
        
        # for i in range(iterations):
        #     self.worst_runtime_rules()
        #     imgplot = plt.imshow(self.earth)
        #     print(self.earth)
        #     time.sleep(1)

def main():
    world = World()
    world.start_sim()



if __name__ == "__main__":
    main()




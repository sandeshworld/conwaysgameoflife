import Tkinter as tk
import numpy as np
from conway import World
import time

class SimulationGUI:

    def __init__(self, squareLength=10):
        self.size = squareLength
        # variables
        self.gui_earth = np.zeros((squareLength,squareLength))
        
        self.window = tk.Tk()
        self.window.geometry("1200x900")
        self._setup_frames(squareLength)
        
        self._interactive_grid(squareLength)    
        self._user_options()
        

    # setup frames to have a display frame and a user buttons frame
    def _setup_frames(self, length):
        # will keep window size the same no matter the number of buttons but will change button size
        static_length = 150
        # pixel frame
        self.displayFrame = tk.Frame(self.window,height=static_length, width=static_length)
        self.displayFrame.pack(side="top")
        # options frame
        self.bottomFrame = tk.Frame(self.window,height=10, width=static_length) # create a frame that will be at the bottom
        self.bottomFrame.pack(side = "bottom")



    def _interactive_grid(self, length):
        #dynamic button creation using lambda function
        buttonSize = int(20/length)
        self.pixels = {}
        for i in range(length):
            for j in range(length):
                self.pixels[(i,j)] = tk.Button(self.displayFrame, height=buttonSize, width=buttonSize, bg="white", command=lambda k = (i,j): self.pixelClick(k))
                self.pixels[(i,j)].grid(row=i,column=j)


    def pixelClick(self, (i,j)):
        self.pixels[(i,j)].configure(bg="red")
        self.gui_earth[i][j] = 1
        print self.gui_earth

        #print(str(x) + str(y) + "was clicked")

    def _user_options(self):
        startSimButton = tk.Button(self.bottomFrame, bg="yellow",height=5, text="START SIM", command=self._startSim)
        startSimButton.pack(side = "left")
        resetSimButton = tk.Button(self.bottomFrame, bg="yellow", height=5, text="RESET", command=self._resetSim)
        resetSimButton.pack(side = "right")


    def _startSim(self):
        print("starting sim")
        for i in self.pixels:
            self.pixels[i].configure(state="disabled")
        # initialize world, where the backend conway sim rules are run
        self.world = World(self.gui_earth)
        self._displayLoop()
    
    def _displayLoop(self):
        self.gui_earth = self.world.run_interation()
        self.updateDisplay()
        self.window.after(1000,self._displayLoop)

    def _resetSim(self):
        print("reseting sim")
        self.gui_earth = np.zeros((self.size,self.size))
        for i in self.pixels:
            self.pixels[i].configure(bg="white", state="normal")


    def startDisplay(self):
        #last method to call
        self.window.mainloop() # maybe this needs to be controlled by main.py?

    def updateDisplay(self):
        for i in self.pixels:
            print(i)
            if self.gui_earth[i[0],i[1]] == 1:
                self.pixels[i].configure(bg="red")
            else:
                self.pixels[i].configure(bg="white")
            



def main():

    length = input("Enter size of world (0-30): ")
    #add upper and lower limit to length size 
    try:
        length = 10 if length < 10 else 30 if length > 30 else length
    except:
        print("Enter a proper number next time.")
        print("10 chosen as default.")
        length = 10

    try:
        simSpeed = int(input("Enter simulation speed (1 -> slowest, 5 -> fastest"))
        simSpeed = 1 if simSpeed < 1 else 5 if simSpeed > 5 else simSpeed
    except:
        print("Enter a proper number between 1 and 5 next time.")
        print("1 chosen as default.")
        simSpeed = 1
    
    gui = SimulationGUI(squareLength=length)
    gui.startDisplay()


if __name__ == "__main__":
    main()
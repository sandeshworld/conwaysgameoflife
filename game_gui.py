import Tkinter as tk



class SimulationGUI:

    def __init__(self):
        self.window = tk.Tk()
        self._setup_frames()
        self._interactive_grid()    
        self.startDisplay()  

    # setup frames to have a display frame and a user buttons frame
    def _setup_frames(self):
        self.topFrame = tk.Frame(self.window,height=1000, width=100)
        self.topFrame.pack(side = "top")
        self.bottomFrame = tk.Frame(self.window,height=1000, width =1000) # create a frame that will be at the bottom
        self.bottomFrame.pack(side = "bottom")


    def _interactive_grid(self, squareLength = 10):
        #dynamic button creation using lambda function
        for i in range(squareLength):
            for j in range(squareLength):
                b = tk.Button(self.topFrame, bg="white", command=lambda k = (i,j): self.pixelClick(k))
                b.grid(column=i,row=j)


    def pixelClick(self, (x,y)):
        print(str(x) + str(y) + "was clicked")
        
    def startDisplay(self):
        #last method to call
        self.window.mainloop() # maybe this needs to be controlled by main.py?
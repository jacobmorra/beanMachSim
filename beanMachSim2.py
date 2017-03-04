import random as r
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#have n bins, n-1 pins at bottom row, then n-2, n-3...

class beanMachSim():
    def __init__(self, numBalls):
        self.numBalls = numBalls
        self.numRows = 20
        self.numBins = self.numRows+1
        self.binContents = np.zeros((self.numBins,), dtype=np.int)
        self.ballPos = 0

    def theorResult(self):
        return True

    def moveRight(self):
        p = np.random.rand()
        if p > 0.5 and p < 1:
            #print p
            return True

        elif p > 0 and p <= 0.5:
            #print p
            return False

    def dropBall(self):
        self.ballPos = (self.numBins/2)+1 #reset ball pos to middle b/w 0 and 9
        print "start @ middle: ", self.ballPos
        for i in range(self.numRows+1):
            print "row: ", i
            right = self.moveRight()
            if right is True:
                if self.ballPos == self.numBins-1:
                    print "ball @ 9"
                    pass
                elif self.ballPos < self.numBins-1:
                    print "move right"
                    self.ballPos += 1
            if right is False:
                if self.ballPos == 0:
                    print "ball @ 0"
                    pass
                elif self.ballPos > 0:
                    print "move left"
                    self.ballPos -= 1
            print self.ballPos

        return self.ballPos

    def dropAllBalls(self):
        while self.numBalls > 0:
            self.binContents[self.dropBall()] += 1
            self.numBalls -= 1
    def update_hist(self):
        plt.cla() #clear axis
        for i in self.binContents:
           self.binContents[i] +=1
        plt.hist(self.binContents)



def main():
    import random as r
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    q = beanMachSim(1000)
    q.dropAllBalls()
    print q.binContents

    numFrames = 10

    #plt.bar(range(0, q.numBins), q.binContents)
    #plt.show()

    number_of_frames = 10

    fig = plt.figure()
    ax1=fig.add_subplot(1,1,1)
    #hist = plt.hist(q.binContents[0])

    def animate(i):
        a=beanMachSim(100)
        x=[]
        for i in range(a.numBins):
            x.append(i)
        while a.numBalls > 0:
            print a.binContents
            a.binContents[a.dropBall()] += 1
            a.numBalls -= 1
            print a.binContents
        #plt.hist(a.binContents)
        ax1.plot(x,a.binContents)

    ani = animation.FuncAnimation(fig, animate, interval = 100)
    plt.show()
if __name__ == "__main__": main()
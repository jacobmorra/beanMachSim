import random as r
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class beanMachSim():
    def __init__(self, numBalls):
        self.numBalls = numBalls
        self.numRows = 9
        self.numBins = 10
        self.binContents = [0,0,0,0,0,0,0,0,0,0]
        self.ballPos = 0

    def moveRight(self):
        p = r.random()
        if p > 0.5 and p < 1:
            #print "yo"
            return True
        elif p > 0 and p <= 0.5:
            #print "hi"
            return False

    def dropBall(self):
        self.ballPos = 4 #reset ball pos to middle b/w 0 and 9
        for i in range(self.numRows):
            if self.moveRight() is True:
                if self.ballPos == 9:
                    pass
                elif self.ballPos < 9:
                    self.ballPos += 1
            elif self.moveRight() is False:
                if self.ballPos == 0:
                    pass
                elif self.ballPos > 0:
                    self.ballPos -= 1
        return self.ballPos

    def dropAllBalls(self):
        while self.numBalls > 0:
            self.binContents[self.dropBall()] += 1
            self.numBalls -= 1



def main():
    q = beanMachSim(10000)
    q.dropAllBalls()
    print q.binContents
    xbin = [0,1,2,3,4,5,6,7,8,9]

    print q.binContents[1]
    import matplotlib.pyplot as plt
    plt.bar(range(0, 10), q.binContents)
    plt.show()
    #plt.hist(xbin, bins=10, weight=q.binContents)
    ## plt.hist([q.binContents[0],q.binContents[1],q.binContents[2],q.binContents[3], q.binContents[4], q.binContents[5], q.binContents[6], q.binContents[7],q.binContents[8], q.binContents[9]], bins=[0,1,2,3,4,5,6,7,8,9], weights=[1,1,1,1,1,1,1,1,1,1])
    #plt.hist([1, 11, 21, 31, 41, 51, 61, 71, 81, 91], bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[0,1,1,1,1,1,1,1,1,1])
    plt.show()
if __name__ == "__main__": main()
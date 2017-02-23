import random as r

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
    q = beanMachSim(1000)
    q.dropAllBalls()
    print q.binContents

if __name__ == "__main__": main()
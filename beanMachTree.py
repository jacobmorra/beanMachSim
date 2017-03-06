import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    # Return height of tree rooted at this node.
    def depth(self):
        if self.l == None and self.r == None:
            return 1
        elif self.l == None:
            return self.r.depth() + 1
        elif self.r == None:
            return self.l.depth() + 1
        else:
            return max(self.l.depth(), self.r.depth()) + 1


class Tree:
    def __init__(self):
        self.root = None


    #print total tree depth from root
    def tdepth(self):
        if self.root is not None:
            return self.root.depth()

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            # go left
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            # go right
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            i = 0
            while i < self.tdepth:
                if node.depth() == self.tdepth():
                    print str(node.v) + ' ' + str(node.depth())
                elif node.depth() == self.tdepth() - 1:
                    print str(node.v) + ' ' + str(node.depth())
                elif node.depth() == self.tdepth() - 2:
                    print str(node.v) + ' ' + str(node.depth())
                elif node.depth() == self.tdepth() - 3:
                    print str(node.v) + ' ' + str(node.depth())
            print str(node.v) + ' ' + str(node.depth())
            self._printTree(node.l)
            self._printTree(node.r)


'''
class beanMachSim():
    def __init__(self, numBalls, numRows):
        self.numBalls = numBalls
        self.numRows = numRows
        self.numBins = numRows + 1
        self.binContents = np.zeros((self.numBins,), dtype=np.int)
        self.ballPos = 0

    def moveBall(self):
        p = np.random.rand()
        if p > 0.5 and p < 1:
            # print p
            return True

        elif p > 0 and p <= 0.5:
            # print p
            return False

    def dropBall(self):
        self.ballPos = (self.numBins / 2) + 1  # reset ball pos to middle b/w 0 and 9
        print "start @ middle: ", self.ballPos
        for i in range(self.numRows + 1):
            print "row: ", i
            right = self.moveRight()
            if right is True:
                if self.ballPos == self.numBins - 1:
                    print "ball @ 9"
                    pass
                elif self.ballPos < self.numBins - 1:
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
        plt.cla()  # clear axis
        for i in self.binContents:
            self.binContents[i] += 1
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

    # plt.bar(range(0, q.numBins), q.binContents)
    # plt.show()

    number_of_frames = 10

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    # hist = plt.hist(q.binContents[0])

    def animate(i):
        a = beanMachSim(100)
        x = []
        for i in range(a.numBins):
            x.append(i)
        while a.numBalls > 0:
            print a.binContents
            a.binContents[a.dropBall()] += 1
            a.numBalls -= 1
            print a.binContents
        # plt.hist(a.binContents)
        ax1.plot(x, a.binContents)

    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()

if __name__ == "__main__": main()
'''
#     3
# 0     4
#   2      8
tree = Tree()
tree.add(0)
tree.add(-1)
tree.add(-2)
tree.add(1)
tree.add(2)
tree.printTree()
print tree.tdepth()

#print (tree.find(3)).v
#print tree.find(10)
#tree.deleteTree()
#tree.printTree()
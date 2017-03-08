import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.p = None
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
    def printPretty(self, node):
        if node.depth() == self.tdepth():
            print "---" * (self.tdepth() - node.depth()) + "(" + str(node.v) + ")"
        else:
            print "---" * (self.tdepth() - node.depth()) + "(" + str(node.v) + ")"


    def tdepth(self):
        if self.root is not None:
            return self.root.depth()

    def hasLeft(self, node):
        if node.l is not None:
            return True

    def hasRight(self, node):
        if node.r is not None:
            return True

    def getLeft(self, node):
        if self.hasLeft(node):
            return node.l

    def getRight(self, node):
        if self.hasLeft(node):
            return node.l

    def space(self, node):
        return "     "

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val == 2 * node.v:
            # go left
            node.l = Node(val)
            #if node.l is not None:
            #    self._add(val, node.l)
            #else:
            #    node.l = Node(val)
        if val == 2 * node.v + 1:
            # go right
            node.r = Node(val)
            #if node.r is not None:
            #    self._add(val, node.r)
            #else:
            #    node.r = Node(val)
        else:
            if node.l is not None:
                self._add(val, node.l)
            if node.r is not None:
                self._add(val, node.r)
    """
    #add by rank
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
    """

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
        if(node != None):
            self._printTree(node.l)
            #print str(node.v) + ' ' + str(node.depth())
            self.printPretty(node)
            self._printTree(node.r)

    """def _printTree(self, node):
        if node is not None:
            i = 0
            if node.depth() == self.tdepth():
                print str(node.v) + ' ' + str(node.depth())

                while i < self.tdepth():
                    if self.hasLeft(node) and self.hasRight(node):
                        print str(self.getLeft(node)) + ' ' + str(self.getLeft(node).depth()) + " " + str(self.getRight(node)) + ' ' + str(self.getRight(node).depth())
                        i += 1
    """
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
numRows = 4
#generate appropriate number of elements for proper bin tree
def numElem(r):
    if r == 0:
        return 0
    else:
        return 2**(r-1) + numElem(r-1)
tree = Tree()

total_num_elements = numElem(numRows)

#print total_num_elements

for i in range(1,total_num_elements+1):
    tree.add(i)

tree.printTree()

print "Total depth: ", tree.tdepth()

#print (tree.find(3)).v
#print tree.find(10)
#tree.deleteTree()
#tree.printTree()
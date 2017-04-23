import numpy as np
import matplotlib.pyplot as plt

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implementing a Galton Board Simulation || Course: SOFE 2715 - Data Structures
Instructor: Dr. Shahryar Rahnamayan    || Teaching Assistant: Jonathan Gillett

Group members: Jacob Morra (100395426), Amalnnath Parameswaran (100585138)
               Vrund Shah (100586175), Kevin Apuyan (100561117)

This program implements simulates the process of dropping N balls into a vertical board
containing rows of pegs with one peg added for each row from the top (i.e. a Galton Board).
Each ball eventually lands into a particular bin at the bottom of the board.

Given a sufficiently large N, the results are expected to follow the Central Limit Theorem
(CLT), which proposes an approximately normal distribution.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

"""
The following constants allow for easy modification of the number of balls dropped,
the number of rows in the Galton Board, and the frequency with which a plot is drawn
"""
numBalls = 100                                     #Initialize the number of balls dropped
numRows = 6                                        #Initialize the number of board rows
n_skips = numBalls/100                             #Initialize the number of plots skipped

plot_index = 1                                     #counter for naming the output plots
a = list(range(0, numBalls+1))                     #list for tracking plots
decisions = list()                                 #list which stores each leaf hit
decisions2 = [0 for i in range(2**numRows)]        #list which stores each bin hit
buckets = [0 for i in range(numRows+1)]            #list which counts #hits for each bin


'''
This class serves as an abstraction for each node in a binary tree.
Each node has a value v, left child l, and right child r
'''
class Node:
    def __init__(self, val):
        self.v = val                                # value of node
        self.l = None                               # left child
        self.r = None                               # right child

    '''
    This function returns the depth of a given node in a tree
    '''
    def depth(self):
        if self.l is None and self.r is None:
            return 1
        elif self.l is None:
            return self.r.depth() + 1
        elif self.r is None:
            return self.l.depth() + 1
        else:
            return max(self.l.depth(), self.r.depth()) + 1
'''
This class serves as an abstraction for a binary tree. Each tree has a root r.
This class contains methods for adding tree nodes (addNode), building a tree (makeTree),
printing the tree (printTree), printed the tree in a readable format (printPretty),
determining tree depth (tdepth), determining if a node has left or right children (hasLeft,
has Right), dropping a single ball (dropBall), dropping multiple balls (dropBalls), plotting
(singPlot, multPlot), creating a Pascal Triangle (pascalTriangle), clearing a list (clearList),
and summing list elements (listPartSum).
'''
class BinTree:
    def __init__(self):
        self.root = None #root of tree

    """
    This function manually creates a tree with R rows to represent the pins
    """
    def addNode(self, val, node):
        if self.root is None:
            self.root = Node(1)
        else:
            '''if value is double parent, assign as left child'''
            if val == 2 * node.v:
                # go left
                node.l = Node(val)
            '''if value is double parent + 1, assign as right child'''
            if val == 2 * node.v + 1:
                # go right
                node.r = Node(val)
            else:
                '''otherwise, recursively visit left child and possibly add'''
                if node.l is not None:
                    self.addNode(val, node.l)
                '''otherwise, recursively visit right child and possibly add'''
                if node.r is not None:
                    self.addNode(val, node.r)

    """
    This function manually creates a tree with R rows using self.addNode()
    """
    def makeTree(self, numRows):
        for i in range(1,2**(numRows+1)):
            self.addNode(i,self.root)

    '''
    This function checks for a nonempty tree, then calls _printTree
    '''
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    '''
    This function prints out a given tree, given a starting node
    '''
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.r)
            self.printPretty(node)
            self._printTree(node.l)

    '''
    This function enhances the printout of a given tree with added spacing for clear
    visualization of nodes
    '''
    def printPretty(self, node):
        if node.depth() == self.tdepth():
            print "------" * (self.tdepth() - node.depth()) + "(" + str(node.v) + ")"
        else:
            print "------" * (self.tdepth() - node.depth()) + "(" + str(node.v) + ")"

    '''
    This function determines whether or not a given node has a left child
    '''
    def hasLeft(self, node):
        if node.l is not None:
            return True

    '''
    This function determines whether or not a given node has a right child
    '''
    def hasRight(self, node):
        if node.r is not None:
            return True

    '''
    This function returns the total depth of a given tree
    '''
    def tdepth(self):
        if self.root is not None:
            return self.root.depth()

    """
    This function simulates a single ball drop, from a given node to a tree leaf (bin)
    """
    def dropBall(self, node, d):
        p = np.random.rand()

        '''if not at leaf, i.e. depth < total depth'''
        if d < self.tdepth():
            if self.hasLeft(node) and self.hasRight(node):
                '''if p is between 0 and 0.5, go to left child'''
                if 0 < p < 0.5:
                    self.dropBall(node.l, d + 1)
                '''if p is between 0.5 and 1, go to right child'''
                if 0.5 < p < 1:
                    self.dropBall(node.r, d + 1)
        else:
            '''if ball has reached a particular bin/leaf, append to list'''
            decisions.append(node.v)

    """
    This function simulates multiple ball drops, each from a given node to a tree leaf (bin)
    """
    def dropBalls(self, numBalls,node,d):
        for i in range(1,numBalls + 1):
            self.dropBall(node,d)

    """
    This function maps tree leaf hits (decisions) to bin hits (decisions2), then to bin
    frequencies (buckets).
    Ultimately, it feeds buckets into a single bar graph and skips plotting n_skips times.
    """
    def singPlot(self,index,counter):
        pascal = self.pascalTriangle(numRows) #create a Pascal Triangle

        """
        Map the results from decisions into decisions2, and then into buckets
        """
        for i in range(2**numRows):
            for j in range(len(decisions)):
                if decisions[j] == (i + (2**numRows)):
                    decisions2[i] += 1
        """
        The leftmost bucket corresponds to only 1 tree leaf in all cases.
        The rightmost bucket corresponds to only 1 tree leaf in all cases.
        """
        buckets[0] = buckets[0] + decisions2[0]
        buckets[numRows] = buckets[numRows] + decisions2[(2**numRows)-1]

        """
        Calculates the number of tree leaves which can be fed into each board bin.
        For example, given 3 rows of pins, the Pascal Triangle shows the 4th row (i.e. bins)
        having the following sequence: "1 3 3 1" - 3 leaves correspond to the 2nd bin.
        """
        start=1
        for i in range(1,len(buckets)-1):
            numOfLeaves = pascal[i]
            """a bin is fed from a particular number of leaves based on Pascal's Triangle"""
            buckets[i] = buckets[i]+ self.listPartSum(decisions2,start,start+numOfLeaves-1)
            start+= numOfLeaves

        """
        If this is the [n_skips]th plot, create and save a new corresponding bar graph figure
        """
        if counter%n_skips == 0:
            """This part is standard code from matplotlib documentation for plotting a bar graph"""
            plt.clf()
            plt.rcdefaults()

            objects = np.arange(len(buckets))
            y_pos = np.arange(len(objects))
            performance = []
            for i in range(len(objects)):
                performance.append(buckets[i])

            plt.bar(y_pos, performance, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.xlabel('bin number')
            plt.ylabel('frequency')
            axes = plt.gca()
            axes.set_ylim([0, (numBalls)/2])          #fix the height of the plot to show growth
            plt.title('Galton Board Results')

            """This part is a workaround for preventing animation skips with ImageMagick gifs"""
            if ((int(a[index])) >= 0 and (int(a[index])) < 10):
                plt.savefig('galtonBoard_plots/plot000000%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 10 and (int(a[index])) < 100):
                plt.savefig('galtonBoard_plots/plot00000%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 100 and (int(a[index])) < 1000):
                plt.savefig('galtonBoard_plots/plot0000%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 1000 and (int(a[index])) < 10000):
                plt.savefig('galtonBoard_plots/plot000%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 10000 and (int(a[index])) < 100000):
                plt.savefig('galtonBoard_plots/plot00%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 100000 and (int(a[index])) < 1000000):
                plt.savefig('galtonBoard_plots/plot0%s.png' % (str(a[index])))
            elif ((int(a[index])) >= 1000000 and (int(a[index])) < 10000000):
                plt.savefig('galtonBoard_plots/plot%s.png' % (str(a[index])))

    """
    This function creates and saves multiple plots based on the singPlot function.
    """
    def multPlot(self, numBalls, node, d, counter):
        for i in range(1,numBalls + 1):
            del decisions[:]              #clear the list each time a ball is dropped (result saved)
            self.clearList(decisions2)
            self.dropBall(node,d)         #drop a new ball from depth d (for our purposes, d=1)
            self.singPlot(i,counter)      #for each ball dropped, create a single plot
            counter += 1                  #increase the counter for tracking each plot

    """
    This function generates the final row of a Pascal Triangle, corresponds to number of leaves per bin
    """
    def pascalTriangle(self,rows):
        newValue = 1
        finalRow = [newValue]
        for iteration in range(rows):
            newValue = newValue * (rows - iteration) * 1 / (iteration + 1)
            finalRow.append(newValue)
        return finalRow

    """
    This function clears a given list by filling all list entries with 0's
    """
    def clearList(self, list):
        for i in range(len(list)):
            list[i] = 0

    """
    This function creates a sum of entries in a given list. It's used for converting leaf entries to bins.
    """
    def listPartSum(self,list,a,b):
        s = 0
        for i in range(a,b+1):
            s = s + list[i]
        return s

"""
The main method is used to create a binary tree, print the binary tree, and run a galton board simulation with
plots and animations.
"""
def main():
    """create and print the tree"""
    board1 = BinTree()
    board1.makeTree(numRows)
    board1.printTree()

    """run galton board simulation for numBalls balls"""
    board1.multPlot(numBalls, board1.root, 1, 1)

    """run commands from the console to create gifs from multiple Galton Board plots using ImageMagick software"""
    import os
    os.chdir('C:\Program Files\ImageMagick-7.0.5-Q16')
    os.system(
        'convert.exe -loop 0 -delay 30 C:/Users/100395426/PycharmProjects/source_code/galtonBoard_plots/*.png '
        'C:/Users/100395426/PycharmProjects/source_code/galtonBoard_plots/plot.gif')

if __name__ == "__main__":
    main()


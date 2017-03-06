class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

########### CREATE TREE ###########
class Tree:
    def __init__(self):
        self.root = None
    # END _init_

########### DELETE TREE ###########
    def DeleteTree(self):
        self.root = None
    # END DeleteTree.

########### ISEMPTY TREE ###########
    def IsEmpty(self):
        return self.root == None
    # END IsEmpty.

########### DISPLAY TREE ###########
    def PrintTree(self):
        if(self.root != None):
            self._PrintTree(self.root)
    # END PrintTree.

    def _PrintTree(self, node):
        if(node != None):
            self._PrintTree(node.left)
            print(str(node.value) + ' ')
            self._PrintTree(node.right)
    # END _PrintTree.

########### FIND NODE ###########
    def find(self, val):
        if(self.root != None):
        # THEN
            return self._find(val, self.root)
        else:
            return None
        # ENDIF;
    # END find.

    def _find(self, val, node):
        if(val == node.value):
        # THEN
            return node
        elif(val < node.value and node.left != None):
        # THEN
            self._find(val, node.left)
        elif(val > node.value and node.right != None):
        # THEN
            self._find(val, node.right)
        # ENDIF;
    # END _find.

########### INSERT NODE ###########
    def add(self, val):
        if(self.root == None):
        # THEN
            self.root = Node(val)
        else:
            self._add(val, self.root)
        # ENDIF;
    # END add.

    def _add(self, val, node):
        if(val < node.value):
        # THEN
            if(node.left != None):
            # THEN
                self._add(val, node.left)
            else:
                node.left = Node(val)
            # ENDIF;
        else:
            if(node.right != None):
            # THEN
                self._add(val, node.right)
            else:
                node.right = Node(val)
            # ENDIF;
        # ENDIF;
    # END _add;

########### GET ROOT ###########
    def getRoot(self):
        return self.root
    # END getRoot.

########### MAIN PROGRAM ###########

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
print("@@@@@@@@@@@@")
tree.PrintTree()
print("@@@@@@@@@@@@")
print((tree.find(3)).value)
print(tree.find(10))
tree.DeleteTree()
tree.PrintTree()
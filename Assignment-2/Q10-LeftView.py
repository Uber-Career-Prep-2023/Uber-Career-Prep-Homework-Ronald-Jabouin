import BinarySearchTree as BST

# Given a binary tree, create an array of the left view 
# (leftmost elements in each level) of the tree.


# Logic For Solving:
# Level Order traversal and looking for left most value


# Technique: Brute Force / Checking All Nodes
# ST Complexity: 

# Time:


def leftView(tree: BST.BinarySearchTree):
    
    # initialize return array and add the root data
    toReturn = []
    toReturn.append(tree.root.data)

    # At a node, see if theres a left. if there is, add it to the array
    # if theres no left but a right, go left as possible from here


    return toReturn
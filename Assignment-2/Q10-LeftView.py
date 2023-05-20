import BinarySearchTree as BST

# Given a binary tree, create an array of the left view 
# (leftmost elements in each level) of the tree.


# My Logic For Solving:
# Level Order traversal add first value of each level to a list


# Technique: Level-order (breadth-first) traversal
# ST Complexity: 

# Time:


# 1 idea
# BFS of sub arrays. Take each  first element of sub arrays
# 1st array of level 1, 2nd array for lvl2, ...

def leftView(tree: BST.BinarySearchTree):
    
    # initialize return array and add the root data
    toReturn = []
    level = 1

    # At a node, see if theres a left. if there is, add it to the array
    # if theres no left but a right, go left as possible from here


    
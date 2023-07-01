import BinarySearchTree as BST
import collections


# Given a binary tree, create an array of the left view 
# (leftmost elements in each level) of the tree.


# My Logic For Solving:
# BFS / Level order traversal
# Use a queue to keep track of the different levels


def leftView(root: BST.BSTNode):
    
    # initialize return array and add the root data
    toReturn = []
    queue = collections.deque([root])

    # while the queue is not empty
    while queue:
        leftSide = None
        for i in range(len(queue)):
            currNode = queue.popleft()
            if currNode:
                leftSide = currNode
                queue.append(currNode.right)
                queue.append(currNode.left)
        
        # Check that left side is not null before appending
        if leftSide:
            toReturn.append(leftSide)

        return toReturn




    
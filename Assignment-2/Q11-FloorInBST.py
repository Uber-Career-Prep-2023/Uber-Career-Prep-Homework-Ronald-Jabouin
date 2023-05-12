import BinarySearchTree as BST

# Given a target numeric value and a binary search tree, return the floor 
# (greatest element less than or equal to the target) 
# in the BST.


# Logic For Solving:
# Go through every node in the tree and see it's absolute value
# difference to the target value. Return the value with the lowest
# absolute difference to the target node.



# Technique: Brute Force / Checking All Nodes
# ST Complexity: 
#   O(n): go through the list once
#   O(1) operations for adding and checking values in set
    # overall: O(n)
# Time: 30 minutes


def floorInBST(rootNode: BST.BSTNode, targetVal: int):
    
    # initialize closest diff as target value so you have
    # a consistent baseline for all cases
    closestDiff = targetVal
    returnValue = targetVal

    # Base Case:
    # The nodes data is equal to target value
    if rootNode.data == targetVal:
        return rootNode.data
    else:
        # Calculate difference from target value and roots data
        # If a new number is closer, want to make that the new 
        # return value
        if abs(targetVal-rootNode.data) < closestDiff:
            returnValue = rootNode.data

    # Recursive Cases:
    # compare value of children with k to find closest number
    if rootNode.left != None:
        floorInBST(rootNode.left)

    if rootNode.right != None:
        floorInBST(rootNode.right)


    return returnValue




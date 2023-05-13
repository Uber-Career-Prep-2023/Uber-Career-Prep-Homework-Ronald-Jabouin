import BinarySearchTree as BST

# Given a binary tree, create a deep copy. Return the root of the new tree.

# Logic For Solving:
# DFS on the tree and add each node to the new tree. Recursrively call
# function on a nodes children if it has any


# Technique: Generic Search
# ST Complexity: O(N) since I check all nodes
# Time: 15 minutes



        
def deepCopy(node: BST.BSTNode, newTree: BST.BinarySearchTree):
    
    # Add node to new tree
    newTree.insert(node.data)
    
    if node.left != None:
        # add nodes left child to tree if it has one
        deepCopy(node.left)

    if node.right != None:
        # add nodes right child to tree if it has one
        deepCopy(node.right)

    return newTree.root

    
# TODO: Test Cases
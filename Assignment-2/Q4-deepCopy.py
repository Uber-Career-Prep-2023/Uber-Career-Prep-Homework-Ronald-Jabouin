import BinarySearchTree as BST

# Given a binary tree, create a deep copy. Return the root of the new tree.

# Logic For Solving:
# At each node, copy its data and left and right and add that to a 
# new tree


# Technique: Generic Search
# ST Complexity: O(N) since I check all nodes
# Time: 30 minutes


def deepCopy(tree: BST.BinarySearchTree):
    
    newTree = BST.BinarySearchTree(root=tree.root.data)

    if tree.root.left != None:
        newTree.root.left = tree.root.left

# TODO: Test Cases
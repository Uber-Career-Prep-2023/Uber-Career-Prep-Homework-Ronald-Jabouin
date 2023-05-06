
import BinarySearchTree as BST

# Given a binary tree, determine if it is a binary search tree.

# Logic For Solving:
# - if checking a left child node, value should be less
# than it's parent node.
# - invariant in regards to tree root node should hold up as well
# ie: if a value is to the left of a node in a right subtree, that left
# value should still be greater than the root node since its to the right



# Technique: Generic Search
# ST Complexity: O(N) since I check all nodes
# Time: 30 minutes

rootNode = BST.BSTNode(12)
tree = BST.BinarySearchTree(rootNode)

def isBST(tree: BST.BinarySearchTree):
    
    if tree.root == None:
        return True
    
    # Get lowest and highest value for tree rooted at node
    maxLeft = tree.min
    minRight = tree.max

    # Making sure all values to right of node are greater
    # and all values to left are smaller
    if maxLeft > tree.root.data or minRight < tree.root.data:
        return True
    
    return False


# TODO: Test Cases

def main():

# Test 1 - Expect True
    rootNode = BST.BSTNode(10)
    tree = BST.BinarySearchTree(rootNode)  
    eight = BST.BSTNode(8) 
    rootNode.left = eight
    nine = BST.BSTNode(9) 
    eight.right = nine
    sixteen = BST.BSTNode(16)
    rootNode.right = sixteen
    thirteen = BST.BSTNode(13) 
    seventeen = BST.BSTNode(17)
    sixteen.left = thirteen
    sixteen.right = seventeen
    twenty = BST.BSTNode(20)
    seventeen.right = twenty

    print(isBST(tree)) 


    # Test 2 - Expect False
    fifteen = BST.BSTNode(15)
    seventeen.right = fifteen
    print(isBST(tree)) 


main()
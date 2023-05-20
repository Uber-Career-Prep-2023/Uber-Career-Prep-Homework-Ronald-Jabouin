class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root: BSTNode):
        self.root = root

    # // returns the minimum value in the BST
    # recursively check left node until a left node has no child
    def min(self):
        if self.root.left == None:
            return self.root.data

        if self.root.left != None:
            return min(self.root.left)

    # // returns the maximum value in the BST
    # recursively check right node until a right node has no child
    def max(self):
        if self.root.right == None:
            return self.root.data
        
        if self.root.right != None:
            return max(self.root.right)
    
    
    # // returns a boolean indicating whether val is present in the BST
    def contains(self, val:int):

        if self.root.data == val:
            return True

        # Recursively check right children
        if self.root.right != None:
            self.contains(self.root.right)
        
        # Recursively check left children
        if self.root.left != None:
            self.contains(self.root.left)

        # If all nodes have been checked and none of the data equal the target val
        # return false
        return False
    
    # // For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    # // creates a new Node with data val in the appropriate location
    def insert(self, val: int):
        if self.contains(val):
            print("Value is already in tree")
        newNode = BSTNode(val)
    # TODO: implement rest of logic to properly place it into the tree
    
    # // deletes the Node with data val, if it exists
    def delete(self, val: int):
        if not self.contains(val):
            raise Exception("Value not in tree")
    # TODO: implement rest of logic
        # need to handle rebalancing tree properly
    



def positionOf(head: BSTNode, target: BSTNode ):
    # position = 1
    # if head == target:
    #     return position
    
    # currNode = head

    # while currNode.hasNext:
    #     currNode = currNode.next
    #     position += 1
    #     if currNode == target:
    #         return position
        
    # Recursively
    if head == None:
        raise Exception("Null")
    
    if head == target:
        return 1
    
    positionOf(head.next, target)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # // creates new Node with data val at front; returns new head
    def insertAtFront(self, head: Node, val: int):
    #    if there is already a head, have to insert this new element
    # before it and point it to the previous head
        if self.head != None:
            head.next = self.head
            self.head = head
            head.data = val
            self.size += 1
            return head
    # no previous head so head is now just the new node 
        else:
            self.head = head
            head.data = val
            self.size += 1
            return head
        
    # // creates new Node with data val at end
    def insertAtBack(self, val: int):
        newNode = Node(val)
        if self.tail != None:
            self.tail.next = newNode
            self.size += 1
        else:
            self.tail = newNode
            self.size += 1


    # // creates new Node with data val after Node loc
    def insertAfter(self, val: int, loc: Node):
        newNode = Node(val)

        currNode = self.head

        while currNode != loc:
            currNode = currNode.next
        
        if currNode == loc:
            # get current loc next
            temp = loc.next

            # set loc next to newNode
            loc.next = newNode

            # set newNode next to current loc next
            newNode.next = temp

            self.size += 1

    # // removes first Node; returns new head
    def deleteFront(self):
        # moves head pointer to current heads next value
        self.head = self.head.next
        self.size -= 1
        return self.head
    
    # // removes last Node
    def deleteBack(self):
        self.tail = self.tail.prev
        self.size -= 1

    # // deletes Node loc; returns head
    def deleteNode(self, loc: Node):
        currNode = self.head

        while currNode != loc:
            currNode = currNode.next
        
        if currNode == loc:
            # set previous node's next value to be the next node
            currNode.prev.next = currNode.next

        return self.head
    
    # // returns length of the list
    def length(self):
        return self.size
    
    # // reverses the linked list iteratively
    # TODO
    def reverseIterative(self):
        pass
    
    # // reverses the linked list recursively (Hint: you will need a helper function)
    def reverseRecursive(self):
        pass

    

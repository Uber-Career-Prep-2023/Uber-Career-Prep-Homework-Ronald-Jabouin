


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



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

    # creates new Node with data val at end
    def insertAtBack(self, head: Node, val: int):
        if self.tail != None:
            # point the current tail to the new tail
            self.tail.next = head
            # set the data of the new tail
            head.data = val
            # set the tail to the new tail node
            self.tail = head
            self.size += 1
        else:
            self.tail = head
            head.data = val
            self.size += 1

    # // creates new Node with data val after Node loc
    def insertAfter(self, head: Node, val: int, loc: Node):
        newNode = Node(val)
        currNode = self.head

        while currNode != loc:
            currNode = currNode.next
        
        if currNode == loc:
            if loc.next == None:
                loc.next = newNode
                self.size += 1
            else:
                temp = loc.next
                loc.next = newNode
                newNode.next = temp
                self.size += 1

    

    # // removes first Node; returns new head
    def deleteFront(self):
        if self.head != None:
            self.head = self.head.next
            self.size -= 1

            return self.head
        else:
            raise Exception("Nothing to remove")
        

    # removes tail
    def deleteBack(self):
        if self.tail != None:
            self.tail = None
            self.size -= 1


    # // deletes Node loc; returns head
    def deleteNode(self, loc: Node):
        currNode = self.head
        
        while currNode != loc:
            currNode = currNode.next
        
        currNode.next = loc.next
        return self.head

    # return size of linkedlist
    def length(self):
        return self.size
    
    # reverses the linked list iteratively
    def reverseIterative(self):
        prev = None
        currentNode = self.head
        while currentNode != None:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev
         

    def reverseRecursive(self, root): 
        if self.head == None:
            return None
       
        nextNode = reverseRecursive(self,self.head.next)
        
        if self.head.next != None:
            root = self.node
            return root
        
        nextNode.next = self.node
        return self.node

        


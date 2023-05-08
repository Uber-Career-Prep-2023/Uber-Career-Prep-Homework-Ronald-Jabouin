import DoublyLinkedList as LL

# Given a singly linked list, disconnect the cycle, if one exists


# Logic For Solving:
# Traverse the linkedlist and keep track of values in a set until I reach tail.
# If the tail's next value is in the set, set its next pointer to null,
# otherwise do nothing. My implementation of the singly linked list
# keeps track of the tail. Additionally, the cycle could only originate 
# from the tail


# Technique: Standard List Traversal
# ST Complexity: 
#   O(n): go through the list once
#   O(1) operations for adding and checking values in set
    # overall: O(n)
# Time: 15 minutes


def disconnectCycle(list: LL.LinkedList):
    
    currNode = list.head
    mySet = set()

    while currNode.next != None:
        mySet.add(currNode.data)
        currNode = currNode.next
    
    if list.tail.next in mySet:
        list.tail.next = None
import BinarySearchTree as BST
import LinkedList as LL

# Given a singly linked list, move the nth from the last element to the front of the list.


# Logic For Solving:
# pos of element is length - k + 1
    # ex: 2nd to last element in list of size 9 is length - 2 + 1
# pos prev = length - 2
# set for pos's prev node, set its next to pos's next
# set pos to head and its next to the original head


# Technique: 
# ST Complexity: O(n^2) - go through the list twice and in worst case
# I could traverse almost the entire list twice
# Time: 30 minutes

def moveNth(list: LL.LinkedList, nth: int):

    pos = list.length - nth + 1
    posPrev = list.length - nth 

    currNode = list.head
    count = 1

    # Traverse through list to get to nth term
    while count != pos:
        currNode = currNode.next
        count += 1
    
    # Get nth terms original next value
    tempNext = currNode.next

    # Get to nth terms prev node
    count2 = 0
    currNode2 = list.head
    while count2 != posPrev:
        currNode2 = currNode2.next
        count2 += 1
    
    # Set nth terms prev node = to nth terms next value
    currNode2.next = tempNext

    # Get original head, set head to nth term, set nth term next to original head
    originalHead = list.head
    list.head = currNode
    currNode.next = originalHead



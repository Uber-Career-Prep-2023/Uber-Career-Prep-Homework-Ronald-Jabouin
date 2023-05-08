import DoublyLinkedList as LL

# Given a doubly linked list, determine if it is a palindrome.


# Logic For Solving:
# Traverse the linkedlist and keep track of values until I reach head.
# Check if the string or array is the same normal as backwards


# Technique: 
# ST Complexity: O(n) - go through the list once
# Time: 20 minutes


def isPalindrome(list: LL.LinkedList):
    # Track head 
    head = list.head

    # Tracking head for traversing
    currNode = list.head

    # Helper variable to know when to stop
    seen = 0

    # Building string of values to check at end
    result = ""
    
    # Need seen to be 2 to account for starting at head
    # if seen is 2, its the second time around the list
    while seen != 2:
        if currNode == head:
            seen += 1
        result += currNode.data
        currNode = currNode.next
    
    # Simple way to check if the string is the same backwards
    return result == result[::-1]
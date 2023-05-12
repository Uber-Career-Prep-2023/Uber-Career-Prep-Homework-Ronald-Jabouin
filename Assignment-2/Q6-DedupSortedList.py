import LinkedList as LL
# # Given a sorted singly linked list, remove any duplicates 
# so that no value appears more than once.

# Logic For Solving:
# Go through the list and at each node, check if its
# value is in the set. if its not, add it to the set and continue
# if it is, delete the node



# Technique: Hashed Linked List Nodes
# ST Complexity: 
#   Time: O(N) because I check each node. Set operations are constant
    # Space: O(N) size of set could be the size of whole list
# Time: 

def dedupSortedList(list: LL.LinkedList):
    currNode = list.head
    mySet = set()

    while currNode.next != None:
        if currNode.data in mySet:
            list.deleteNode
        else:
            mySet.add(currNode.data)
        
        currNode = currNode.next



# TODO: Test Cases
def main():

# Test 1 - Expect True
# 1,2,2,4,5,5,5,10,10

    node9 = LL.Node(10, None)
    node8 = LL.Node(10, node9)
    node7 = LL.Node(5, node8)
    node6 = LL.Node(5, node7)
    node5 = LL.Node(5, node6)
    node4 = LL.Node(4, node5)
    node3 = LL.Node(2, node4)
    node2 = LL.Node(2, node3)
    node1 = LL.Node(1, node2)
    newList = LL.LinkedList()
    newList.insertAtFront(node1)
    newList.insertAtBack(node3)
    newList.insertAtBack(node4)
    newList.insertAtBack(node5)
    newList.insertAtBack(node6)
    newList.insertAtBack(node7)
    newList.insertAtBack(node8)
    newList.insertAtBack(node9)

    print(f"List Before: {newList}")
    dedupSortedList(newList)
    print(f"List After: {newList}")

main()
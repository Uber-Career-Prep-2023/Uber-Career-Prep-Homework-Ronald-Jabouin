

# Given a number, k, return an array of the first k binary numbers, represented as strings.
# Time: 35 minutes
# Implementation: Queue
#   pattern of removing and enqueing 1s and 0s
    # Start with 1 and add 0 to the beginning at the end


# dequeu, enqueu with 0 and 1

from collections import deque

def binaryNumbers(k: int):

    # Init queue and counter
    # start with 1 in queue
    myQueue = deque()
    myQueue.append("1")
    
    # hard code first 0, start algo at 1 
    result = []
    result.append("0")
    
    counter = 1

    while counter < k:
        #add current value plus 0 
        myQueue.append(myQueue[0] + "0")
        # add current value plus 1 at end
        myQueue.append(myQueue[0] + "1")
        # pop oldest value and add it to result 
        temp = myQueue.popleft()
        result.append(temp)
        counter += 1
    
    return result
    

print(binaryNumbers(5))
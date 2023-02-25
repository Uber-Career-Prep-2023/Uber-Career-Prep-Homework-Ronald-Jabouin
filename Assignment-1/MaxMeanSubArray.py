
# Technique: Fixed Sliding Window
# Time Complexity: DNF
# Time Spent: 40 minutes


"""
Test Inputs and Outputs:

Array: [4,5,-3,2,6,1]
k = 2
Output: 4.5

Array: [4,5,-3,2,6,1]
k = 3
Output: 3

Array: [1,1,1,1,-1,-1,2,-1,-1,6]
k = 3
Output: 1

Array: [1,1,1,1,-1,-1,2,-1,-1,6]
k = 4
Output: 1.5
"""

# Notes and Thoughts

# Start at 0 and have 2nd pointer be k-1
# Mean = element + element ... / k


def MaxMeanSubArray(arr, k):
    #variable to update as new values are computed
    largestMean = 0
    
    # Pointer starting at 0
    for x in arr:
        print(f"x is {x}")

        #if x is not the last position that allows window size to fit in array
        if x is not arr[-k]:
            # FIXME: the x here is not the index, it's the exact value. 
            secondPointer = arr[x+(k-1)]
            print(arr[x])
            print(f"x is {x} and secondPointer is {secondPointer}")
            print(arr[x:secondPointer])
            print("--------")
            meanSum = sum(arr[x:secondPointer])
            mean = meanSum / k

            if mean > largestMean:
                largestMean = mean
    
    # #Pointer starting at k-1
    #     for y in arr[k-1:]:
    #         # print(x+y)
    #         mean = x + y / k
    #         if mean > largestMean:
    #             largestMean = mean
    
    return largestMean

#Reflection:
    # Realized my main issue towards the end while debugging.
    # I was incorrectly calculating indexes and instead getting exact values which
    # threw off my calucations. Example in FIXME comment.
 
 #Future Reference of Solution:
#  https://leetcode.com/problems/maximum-average-subarray-i/solutions/127562/maximum-average-subarray/ 
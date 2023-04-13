
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

    leftPointer = 0
    rightPointer = k
    maxMean = 0
    
    if not arr or len(arr) < k:
        return 

    while rightPointer < len(arr) + 1:
        maxMean = max(maxMean, sum(arr[leftPointer:rightPointer]) / k)
        leftPointer += 1
        rightPointer += 1
    return maxMean

if __name__ == "__main__":
    print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 2))
    print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 3))
    print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
    print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))


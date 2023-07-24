# Given an array of k sorted arrays, merge the k arrays into a single sorted array.
# Time: 
# Implementation: Brute Force
    # go through arrays adding each value to a list
    # sort final list   
    # time complexity: O(n^2) since I'm iterating through the entirity of the outer and inner lists

# Further Optimization:
    # megre sort algo



def mergeKSortedArrays(k: int, inputList: list):
    result = []
    for sublist in inputList:
        for number in sublist:
            result.append(number)
    
    result.sort()
    return result


print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
# Expected Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
# Expected Output: [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]


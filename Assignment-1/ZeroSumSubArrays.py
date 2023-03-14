# Technique: One directional running
# Time Complexity: O(n)
    # Loop through array once
# Space Complexity: 0(1)
    # Creating a small set
# Time Spent: 30 minutes


# Question 3: ZeroSumSubArrays
# Given an array of integers, count the number of subarrays that sum to zero.

# Examples:
# Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
# Output: 2
# (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

# Input Array: [1, 8, 7, 3, 11, 9]
# Output: 0

# Input Array: [8, -5, 0, -2, 3, -4]
# Output: 2
# (Subarrays: [0], [8, -5, 0, -2, 3, -4])

input = [8, -5, 0, -2, 3, -4]



def zeroSubArrays(input):
    result = 0
    pointer = 0
    mySet = set()
    mySet.add(0)

    for value in input:
        pointer += value
        if pointer in mySet:
            result += 1
        else:
            mySet.add(pointer)

    return result

print(zeroSubArrays(input))
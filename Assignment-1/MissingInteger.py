# Technique: One directional running computation
# Time Complexity: O(n)
    # one for loop through the array
# Space Complexity: O(1)
    # not creating anything new
# Time Spent: 25 minutes


array = [2,3,4,5]
size = 5
def missingInteger(arr, size):

    toReturn = 0

    if size == 2:
        return arr[0] + 1

    for number in range(size-1):
        if arr[number] != number + 1:
            toReturn = number + 1
            return toReturn
        
print(missingInteger(array,size))
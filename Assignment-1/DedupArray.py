# Technique: One direction computation
# Time Complexity: O(n)
    #looping through each element in array
# Space Complexity: 0(n)
    # created set that in worse case is same size of input
# Time Spent: 20 minutes


input = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]


def dedupArray(arr):
    for number in len(arr-1):
        if arr[number+1] == number:
            del number+1
    
    return arr
            


# def dedupArray(arr):
#     mySet = set()

#     for number in arr:
#         mySet.add(number)
    
#     arr = list(mySet) 
    
#     return arr

print(dedupArray(input))
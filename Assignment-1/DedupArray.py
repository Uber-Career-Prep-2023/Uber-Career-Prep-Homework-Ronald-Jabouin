# Technique: 
# Time Complexity: 
# Space Complexity: 

# Time Spent: 


input = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]


def dedupArray(arr):
    mySet = set()
    index = 0
    while index < len(arr):
        if arr[index] in mySet:
            del arr[index]
            index -= 1
        else:
            mySet.add(arr[index])
        index+=1
    return arr
            


# def dedupArray(arr):
#     mySet = set()

#     for number in arr:
#         mySet.add(number)
    
#     arr = list(mySet) 
    
#     return arr

print(dedupArray(input))
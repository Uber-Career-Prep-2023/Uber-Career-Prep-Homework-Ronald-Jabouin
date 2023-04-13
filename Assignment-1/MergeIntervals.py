# Technique: 
# Time Complexity: O(n log n) for sorting
# Space Complexity: O(n) since it's using the size of the input array
# Time Spent: 30 minutes


def mergeIntervals(listOfIntervals):
        
          
    listOfIntervals.sort()
    result = []

    for value in range(1, len(listOfIntervals)):
        if listOfIntervals[value-1][1] >= listOfIntervals[value][0]:
            temp =(listOfIntervals[value-1][0], max(listOfIntervals[value-1][1], listOfIntervals[value][1]))
            listOfIntervals[value] = temp
        else:
            result.append(listOfIntervals[value-1])
            
    result.append(listOfIntervals[-1])
    
    return result

print(mergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))

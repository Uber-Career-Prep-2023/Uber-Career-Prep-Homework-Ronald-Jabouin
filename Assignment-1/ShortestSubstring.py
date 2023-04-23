# Two arrays
# Time Complexity: 
# Space Complexity: 
# Time Spent: 


def ShortestSubstring(input, target):
    if len(target) == 0:
        return 0
    myDict = {}
    for x in target:
        if x in myDict:
            myDict[x] += 1
        else:
            myDict[x] = 1
    
    pointer_head = 0
    pointer_tail = 0
    count = len(myDict)  
    shortest = len(input)
    
    while pointer_tail < len(input):
        tail = input[pointer_tail]
        if tail in myDict:
            myDict[tail] -= 1
            if myDict[tail] == 0:
                count -= 1
        pointer_tail += 1
        while count == 0:
            shortest = min(shortest, pointer_tail - pointer_head)
            head = input[pointer_head]
            if head in myDict and myDict[head] == 0:
                myDict[head] = 1
                count = 1
            pointer_head += 1
    return shortest


if __name__ == "__main__":
    print(ShortestSubstring( "abracadabra","abc"))
    print(ShortestSubstring( "zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx"))
    print(ShortestSubstring( "dog","god"))




    
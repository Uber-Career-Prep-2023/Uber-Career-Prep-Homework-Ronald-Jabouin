# Technique: Forward Backward Two Pointer
# Time Complexity: O(n)
# Time Spent: 40 minutes

""" 
Test Inputs and Outputs:

Input String: "Uber Career Prep"
Modified String: "eber Ceraer PrUp"

Input String: "xyz"
Modified String: "xyz"

Input String: "flamingo"
Modified String: "flominga"
"""
toTest = "flamingo"


def reverseVowels(input):
    vowels ="aeiouAEIOU"
    helperList = list(input)
    i=0
    j=(len(input)-1)
    while i<j:
        while i<j and helperList[i] not in vowels:
            i+=1
        
        while j>i and helperList[j] not in vowels:
            j-=1
        helperList[i],helperList[j]=helperList[j],helperList[i]
        i+=1
        j-=1
    return "".join(helperList)

print(reverseVowels(toTest))


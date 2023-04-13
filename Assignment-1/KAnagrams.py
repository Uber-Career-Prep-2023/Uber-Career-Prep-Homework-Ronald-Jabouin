# Technique: 
# Time Complexity:
# Space Complexity: 
# Time Spent: 

def KAnagrams(word1,word2,k):
    if len(word1) != len(word2): return False
    result = 0
    myMap1,myMap2 = {}, {}

    for letter in word1:
        if letter in myMap1:
            myMap1[letter] +=1
        else:
            myMap1[letter] = 1

    for letter in word2:
        if letter in myMap2:
            myMap2[letter] += 1
        else:
            myMap2[letter] = 1

    for letter in myMap1:
        if letter not in myMap2:
            result += 1
            continue
        if myMap1[letter] != myMap2[letter]: 
            result = result + abs(myMap1[letter] - myMap2[letter])
        if result > k: return False
    
    return True

if __name__ == "__main__":
    print(KAnagrams("apple", "peach", 1))
    print(KAnagrams("apple", "peach", 1))
    print(KAnagrams("apple", "peach", 2))
    print(KAnagrams("cat", "dog", 3))  
    print(KAnagrams("debit curd", "bad credit", 1))
    print(KAnagrams("baseball", "basketball", 2))  
# Technique: Hash the elements
# Time Complexity: O(N). Pass through the list of integers once
# Space Complexity: O(n). Worst case the map contains almost every element from
# original input
# Time Spent: 35 minutes



def twoSum(nums: list[int], target: int) -> list[int]:

    myMap = {}
    toReturn = []
    numOfPairs = 0

    for index in range(len(nums)):
        if target - nums[index] in myMap:
            toReturn.append(index)
            toReturn.append(myMap[target-nums[index]])
            # return toReturn
            numOfPairs += 1
        else:
            myMap[nums[index]] = index

    return numOfPairs

if __name__ == "__main__":
    arr_input = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(twoSum(arr_input, 10))
    # 3


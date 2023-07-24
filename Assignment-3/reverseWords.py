# Given a string, return the string with the order of the space-separated words reversed
# Time: 20 minutes
# Implementation: Stack
    # get each word thats seperated by a space
    # add that to a stack
    # build a new string by adding from the stack

# *had to lookup .split method in python

def reverseWords(inputString: str):
    # split string by spaces. returns a list
    stack = inputString.split(' ')
    print(stack)

    # iterate through this list in reverse and add to a string
    result = ""

    while stack:
        # remove first space from empty result string
        if not result:
            result = result + stack.pop()
        else:
            result = result + ' ' + stack.pop()

    return result


print(reverseWords("Uber Career Prep"))
print(reverseWords("Emma lives in Brooklyn, New York."))
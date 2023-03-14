# Technique: Two arrays
# Time Complexity: O(n^2)
    # Loop through the entirety of two arrays
# Space Complexity: 0(n^2)
    # Create two new arrays which in worst case contain the entirety
    # of the original two strings
# Time Spent: 30 minutes


string1 = "abcdef###xyz"
string2 = "abcdefxyz###"
def backspaceCompare(string1, string2):

    s1NoBackspace = []
    s2NoBackspace = []

    for letter in string1:

      if letter != "#":
         s1NoBackspace += letter
      else:
         del s1NoBackspace[-1]

    
    for letter in string2:
       if letter != "#":
         s2NoBackspace += letter
       else:
         del s2NoBackspace[-1]

    return s2NoBackspace == s1NoBackspace

print(backspaceCompare(string1=string1, string2=string2))
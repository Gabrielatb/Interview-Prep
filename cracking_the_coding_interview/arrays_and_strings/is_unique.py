###QUESTION 1.1###

#implement and algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures.

def unique(string):

    for i, char in enumerate(string):
        concat = string[i+1:]
        if char in concat:
            return False
    return True

print unique('gabriela')

#in this solution I am not using any additional data structures

# time complexity: O(n**2)
# space complexity: O(1)?


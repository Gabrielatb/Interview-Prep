###QUESTION 1.1###

#1. implement an algorithm to determine if a string has all unique characters. 
#2. What if you cannot use additional data structures.

def unique(s):
    """
    >>> unique('abc')
    True

    >>> unique('cabc')
    False

    >>> unique('')
    True

    >>> unique('abc!')
    True

    >>> unique('Dad')
    False
"""

#Not using additional data structure
# Time Complexity: O(nlog(n)) 
# Space Complexity: O(1)
#heap sort 
def heapifu(lst, length, i):
    largest = i
    l = 2 * i +1
    r = 2 * i + 2

[0,1,2,3,4]

def heapsort(lst):

    length = len(lst)

    #building a maxheap
    for i in range(10, -1, -1):
        heapif(lst, length, i)

    #extracting elements



    # s = s.lower()
    # sorted_lst = sorted(s)
    # for i in range(len(sorted_lst)-1):
    #     if sorted_lst[i] == sorted_lst[i+1]:
    #         return False

    # return True



    # seen = []
    # for char in s:
    #     char = char.lower()
    #     if char in seen:
    #         return False
    #     else:
    #         seen.append(char)
    # return True























# Time Complexity: O(n)

# Space Complexity: O(n)


    # seen = []
    # for char in s:
    #     char = char.lower()
    #     if char in seen:
    #         return False
    #     else:
    #         seen.append(char)
    # return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.***\n")

#in this solution I am not using any additional data structures

# time complexity: O(n)
# space complexity: O(1)?
































# def unique(string):

#     for i, char in enumerate(string):
#         concat = string[i+1:]
#         if char in concat:
#             return False
#     return True

# print unique('gabriela')

# Given an array, [1,1,1,1,4,4,4,6,6,6,6,8,8] and an integer z. 
#Return the index of the first occurrence of z in the given array.
# Follow-up: Can you improve run-time if input is sorted?

# Example: For the above array, if z=6, return 7 i.e. 
#the index of the first occurrence of 6 in the array.


def occ(lst, integer):

    for indx, num in enumerate(lst):
        if num == integer:
            return indx
    return None


print occ([1,1,1,1,4,4,4,6,6,6,6,8,8], 6)
# Given an array, [1,1,1,1,4,4,4,6,6,6,6,8,8] and an integer z. 
# Return the index of the first occurrence of z in the given array.
# Follow-up: Can you improve run-time if input is sorted?

# Example: For the above array, if z=6, return 7 i.e. 
#the index of the first occurrence of 6 in the array.



def first_occ(lst, data):

    # for i, num in enumerate(lst):
    #     if num == data:
    #         return i

#Time Complexity: log(n)
#Space Complexity: O(1)
    i = len(lst) /2
    while i < len(lst):
        if lst[i] < data:
            i +=1 
        elif lst[i] > data:
            i-=1
        elif lst[i] == data:
            while i >= 0:
                if lst[i] == data:
                    i-=1
                else:
                    break
            return i+1


print first_occ([1,1,1,1,4,4,4,6,6,6,6,8,8], 6)
























# def occ(lst, integer):

#     for indx, num in enumerate(lst):
#         if num == integer:
#             return indx
#     return None


# print occ([1,1,1,1,4,4,4,6,6,6,6,8,8], 6)
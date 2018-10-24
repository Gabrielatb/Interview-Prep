#deleting repeated elements from a sorted array

#input [2,3,5,5,7,11,11,13]
#output [2,3,5,7,11,13]


#Time: O(n)
#Space: O(1)
def delete_dup(lst):
    if lst == []:
        return 0

   
    write_indx = 1

    for i in range(1, len(lst)):
        if lst[write_indx-1] != lst[i]:
            lst[write_indx] = lst[i]
            write_indx += 1

    print lst
    return write_indx


print delete_dup([2,3,5,5,7,11,11,13])
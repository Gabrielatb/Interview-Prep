# Problem 8.3

def magic_index(lst):
    hi = len(lst) - 1
    return binary_search(lst, hi, lo=0)




def binary_search(lst, hi, lo):
    if lo > hi:
        return -1 
    mid = hi+lo/2

    if lst[mid] == mid:
        return mid

    
    elif lst[mid] > mid:
        return binary_search(lst, mid-1, lo)
    else:
        return binary_search(lst, hi, mid+1)

    return -1




print magic_index([-20, -10, 0, 1, 4,11,12,13,14,15])

#b(lst, 9,0)
#mid = 4
#lst[4] = 10
#b(lst, 3,0)
#mid = 1
#lst[1] = -10
##b(lst, 3,1)
#mid = 2


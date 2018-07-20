#Find position of an element in a sorted array of infinite numbers

#FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE
# THEREFORE, THERE IS NO INDEX OUT OF BOUND CHECKING


def binary_search(lst, value, l, r):

    while low <= high:
        mid = (l + r) / 2
        mid_elem = lst.elementAt(mid)
        if mid_elem == value:
            return mid
        elif mid_elem < value or mid_elem == -1:
            high = mid -1
        else:
            low = mid + 1

    return -1

    if lst[mid] == value:
        return mid
    elif lst[mid] <= lst[high]:
            binary_search(l+1, r,lst, value)
    else:
        lbinary_search(l, r+1,lst, value)



O(logn)




def find_bounds(lst, value):

    index = 1
    while lst.elementAt(i) += -1 and lst.elementAt(i) < value:
        index *=2

    return binary_search(lst, value, index/2, index)





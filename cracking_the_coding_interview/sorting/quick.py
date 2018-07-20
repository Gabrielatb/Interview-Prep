"""This quick sort is written for ease of understanding. A more 
efficient implementation is used in sorts.py."""

def quicksort(lst):
    """Quicksort list and return result."""

    # if length of lst is 1, return lst
    if len(lst) < 2:
        print lst
        return lst


    # select pivot element
    mid = int(len(lst) / 2)  # index at half the list
    pivot = lst[mid]

    # partition elements into lo , hi , eq buckets
    lo , hi , eq = [] , [] , []
    for elem in lst :
        if elem < pivot :
            lo.append(elem)
        elif elem == pivot :
            eq.append(elem)
        else :  #  elem > pivot
            hi.append(elem)

    # concatenate sorted buckets and finish
    return quicksort(lo) + eq + quicksort(hi)

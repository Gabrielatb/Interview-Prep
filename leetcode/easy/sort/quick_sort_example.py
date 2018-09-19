#[5,88,15,2,6]

#P_index
#partition([2*,5,15*,88i*,6], lo=0, hi=4)

def partition(lst, start, end):
    pivot = start

    for i in range(start, end):
        print i

        if lst[i] <= lst[end]:

            lst[i], lst[pivot] = lst[pivot], lst[i]

            pivot += 1

        print lst

    lst[end], lst[pivot] = lst[pivot], lst[end]
    print lst
        

    print 'this is the pivot ', pivot
    print '##############################'
    return pivot

def quicksort_helper(lst, lo, hi):
    print 'inside helper'
    if lo < hi:

        pivot = partition(lst, lo, hi)
        quicksort_helper(lst, pivot+1, hi)

        quicksort_helper(lst, lo, pivot-1)


def quicksort(lst):

    quicksort_helper(lst, 0, len(lst)-1)
    return lst 


print quicksort([5,88,15,2,6])
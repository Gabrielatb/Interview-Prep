#generic quicksort implementation


def quicksort(lst):

    if len(lst) <= 1:
        return lst

    lo, eq, hi = [], [], []

    pivot = len(lst)/2

    for num in lst:
        if num < lst[pivot]:
            lo.append(num)
        elif num > lst[pivot]:
            hi.append(num)
        else:
            eq.append(num)

    return quicksort(lo) + eq + quicksort(hi)



print quicksort([4,7,3,9,0,22,])


#Runtime O(nlogn) average, worst case O(n**2)


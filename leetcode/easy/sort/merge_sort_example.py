# #merge sort implementation from my code school

# Runtime O(nlog(n))
# Space Complexity O(n)

# def merge_sort()

def merge_sort(lst, left, right):
    l_indx = 0
    r_indx = 0
    lst_indx = 0

    while len(left) > l_indx and len(right) > r_indx:
        if left[l_indx] < right[r_indx]:
            lst[lst_indx] = left[l_indx]
            l_indx +=1
            lst_indx +=1
        else:
            lst[lst_indx] = right[r_indx]
            r_indx +=1
            lst_indx +=1
    while len(left) > l_indx:
        lst[lst_indx] = left[l_indx]
        l_indx +=1
        lst_indx +=1
    while len(right) > r_indx:
        lst[lst_indx] = right[r_indx]
        r_indx +=1
        lst_indx +=1
    return lst

def merge(lst):

    if len(lst) < 2:
        return lst

    mid = len(lst) / 2

    left = lst[:mid]

    right = lst[mid:]

    merge(left)
    merge(right)
    merge_sort(lst, left, right)
    return lst


print merge([5,4,9,2,1])


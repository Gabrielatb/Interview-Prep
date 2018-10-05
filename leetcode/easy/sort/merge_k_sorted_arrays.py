# Given [[3,5,7], [0,6], [0,6, 28]]
# output = [0,0,3,5,6,6,7,28]

def merge_sort(lst, left, right):
    l_indx = 0
    r_indx = 0
    lst_indx = 0

    while len(left) > l_indx and len(right) > r_indx:
        if left[l_indx] < right[r_indx]:
            lst[lst_indx] = left[l_indx]
            l_indx +=1
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



def single_lst(lsts):
    single_lst = []
    for lst in lsts:
        single_lst += lst
    return merge(single_lst)

#Runtime: nlog(nk
#Space: O(n)

print single_lst([[3,5,7], [0,6], [0,6, 28]])
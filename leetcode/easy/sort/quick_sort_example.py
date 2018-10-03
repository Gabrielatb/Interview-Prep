#[5,88,15,2,6]

#[4,3,2*,1,6,7]

# Runtime O(nlog(n))
#Space Complexity O(1)
def partition(lst, start, end):

    pivot = lst[end]
    p_index = start

    for i in range(start, end):
        if lst[i] < pivot:

            lst[i], lst[p_index] =  lst[p_index], lst[i]
            p_index += 1


    lst[p_index], lst[end] = lst[end], lst[p_index]
    return p_index

def quicksort(lst, start, end):

    #if segment invalid, or if segment has one element

    if start < end:


        p_indx = partition(lst, start, end)

        quicksort(lst, start, p_indx -1)
        quicksort(lst, p_indx+1, end)

    return lst

print quicksort([5,4,3,2,1], 0, 4)
















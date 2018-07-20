# #bubblesort implementation


def bubblesort(lst):

    for i in range(len(lst)-1):
        swap = False
        for j in range(len(lst) -1 -i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True

        if swap == False:
                break

    return lst



print bubblesort([22,9,7,4,3,22])
#Heap Sort Implementation


# Runtime O(nlogn)
# Space Complexity O(1)


#Root smallest (min)
#elements get bigger

#min element root node

#remove node, swap with last element added, bubble down

# swap with smallest of the two

#         10(0)
#         /   \
#      5(1)   3(2)
#     /   \
#  4(3)    1(4)
def heapify(lst, n, i):
    largest = i
    #initializing largest element as the root
    l_index = 2 * i + 1 #--> left index

    r_index = 2 * i + 2 #--> right index
    #see if left child exists and is greater than root
    #so if left index less than length of lst

    if l_index < n and lst[largest] < lst[l_index]:
        largest = l_index
    if r_index < n and lst[largest] < lst[r_index]:
        largest = r_index

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i] #swap

        #heapify new root
        heapify(lst, n, largest)

def heapSort(lst):
    n = len(lst)

    #building maxheap
    for i in range(n-1,-1,-1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst

print heapSort([4,10,3,5,1])

#different types of sorting:

# 1. quicksort: implement it, explain it
# 2. mergesort: implement it, talk about space complexity as well as time complexity
# 3. insertion sort: explain when it can be better than the above two
# 4. heapsort: explain how it works, and how heaps work in general
# 5. bubble sort: why it's awful
# 6. radix/counting/bucket sort: when it's useful
# 7. selection sort: usually thrown in as an example when asked to list sorting algorithms you know


# Merge sort, Quick sort, Heap sort and Radix sort.

#Time complexity O(n**2)
#Space Complexity O(1)
def bubblesort(lst):
    #[4,3,2,1]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
 

    return lst


#list
#Time Complexity Worst: O(n**2), AverageO(nlogn)
#Space Complexity O(n)
def quicksort(lst):

    length = len(lst)

    if length < 2:
        return lst

    mid = length / 2
    print "this is my original lst= " + str(lst)
    print "this is my midpoint= " + str(mid)
    pivot = lst[mid]
    print "this is my pivot= " + str(pivot)

    less, greater, eq = [], [], []

    for elem in lst:
        if elem > pivot:
            greater.append(elem)
        elif elem < pivot:
            less.append(elem)
        else:
            eq.append(elem)

    print "less= " + str(less)
    print "greater= " + str(greater)
    print "eq= " + str(eq)
    return quicksort(less) + eq + quicksort(greater)


# Improved Quicksort, randomized pivot
#Average O(nlogn), worst case (On**2) 
#Space O(1)


def partition(lst, start, end):
    pos = start                          
                                         
    for i in range(start, end):           
        if lst[i] < lst[end]:             
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] 
                                      
    return pos

 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr
 
def quicksort(arr):
    return quickSort(arr, 0, len(arr)-1)
# Driver code to test above
arr = [5,15,3,99]
print quicksort(arr)






#Time Complexity: O(nlogn) --> n because we have to iterate over our list (logn because we are dividing and conquering)
#Space Complexity: O(n) --> Creating new list to store values
def merge(lst):

    length = len(lst)

    if length < 2:
        return lst

    mid = len(lst) / 2

    left = lst[:mid]
    right = lst[mid:]


    merge(left)
    merge(right)
    return merge_sort(left,right, lst)


def merge_sort(l, r, nums):
    l_length = len(l)
    r_length = len(r)
    l_indx = 0
    r_indx = 0
    nums_indx = 0


    while l_length > l_indx and r_length > r_indx:
        if l[l_indx] > r[r_indx]:
            nums[nums_indx] = r[r_indx]
            r_indx +=1

        else:
            nums[nums_indx] = l[l_indx]
            l_indx +=1

        nums_indx +=1


    while l_length > l_indx:
        nums[nums_indx] = l[l_indx]
        l_indx +=1

    while r_length > r_indx:
        nums[nums_indx] = r[r_indx]
        r_indx +=1
    return nums
 


#Time: O(nlogn) 
#Space: O(1)
def heap_sort(lst):
    """Add items to binary heap (keeping them in order!) and then extract."""

    def move_down(first, last):
        """Move item down in heap to proper place."""

        # Assume left-hand child is bigger
        largest = 2 * first + 1

        while largest <= last:
            if largest < last and lst[largest] < lst[largest + 1]:
                # Right child exists and is larger than left child
                largest += 1

            if lst[largest] > lst[first]:
                # Selected child is bigger than parent, so swap
                lst[largest], lst[first] = lst[first], lst[largest]

                # Move down to largest child
                first = largest
                largest = 2 * first + 1

            else:
                # Once we don't swap, it's in the right place; exit
                return 

    # Convert lst to heap

    length = len(lst) - 1
    least_parent = length // 2

    for i in range(least_parent, -1, -1):
        move_down(i, length)

    # Flatten heap into sorted array

    for i in range(length, 0, -1):
        if lst[0] > lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
            move_down(0, i - 1)

    return lst


#Heap Sort 
#Min Heap = value each node is less than children
#Max Heap =  value each node is greater than children





#different types of sorting:

# 1. quicksort: implement it, explain it


# 2. mergesort: implement it, talk about space complexity as well as time complexity

# 3. insertion sort: explain when it can be better than the above two
    # - if small list, insertion sort could be more useful becasue do not need recursive stack
    # - time: O(n**2), space: O(1)


# 4. heapsort: explain how it works, and how heaps work in general
    # Useful when you want to maintain a particular order and extract min and max, not useful for arb searches
# 5. bubble sort: why it's awful
    # O(n**2 best runtime)
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

#Runtime O(n**2)
#Space Complexity O(1)
def insertion_sort(lst):

    for i in range(1,len(lst)):
        key = lst[i]

        hole = i

        while hole > 0 and key < lst[hole-1]:
            lst[hole] = lst[hole-1]
            hole -=1
            
        lst[hole] = key

    return lst

print insertion_sort([5,4,3,2,1])
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

# [1.2.3, 4.2.0, 4.11.6, ]

#call quicksort (0, length-1)
#pivot = partition(arr, lo, high)
    #pivot = start
    #for i in start to end
        #if i element < end:
            #pivot + 1
            #swap i, pivot
    #pivot, end
#recursvely call
#quicksort(arr, lo+1, hi)
#quicksort(arr, lo, hi-1) 

'1.2.3'

      # lst_i = lst[i].split('.')
      #   lst_end = lst[end].split('.')


      #   if lst_i[0] < lst_end[0]:
      #       lst[i], lst[pivot] = lst[pivot], lst[i]
      #       pivot +=1
      #   elif lst_i[0] == lst_end[0]:
      #       if lst_i[1] < lst_end[1]:
      #           lst[i], lst[pivot] = lst[pivot], lst[i]
      #           pivot +=1
      #       elif lst_i[1] == lst_end[1]:
      #           if lst_i[2] < lst_end[2]:
      #               lst[i], lst[pivot] = lst[pivot], lst[i]
      #               pivot +=1

def partition(lst, start, end):
    # print 'start list ', lst
    pivot = start

    for i in range(start, end):
        lst_i = lst[i].split('.')
        lst_end = lst[end].split('.')
        if int(lst_i[0]) < int(lst_end[0]):
            lst[i], lst[pivot] = lst[pivot], lst[i]
            pivot +=1
        elif int(lst_i[0]) == int(lst_end[0]):
            if int(lst_i[1]) < int(lst_end[1]):
                lst[i], lst[pivot] = lst[pivot], lst[i]
                pivot +=1
            elif int(lst_i[1]) == int(lst_end[1]):
                if int(lst_i[2]) < int(lst_end[2]):
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    pivot +=1

    lst[end], lst[pivot] = lst[pivot], lst[end]
    # print 'end list ', lst
    return pivot

def quicksort_helper(lst, lo, hi):
    if lo < hi:

        pivot = partition(lst, lo, hi)

        quicksort_helper(lst, pivot+1, hi)

        quicksort_helper(lst, lo, pivot-1)

        return lst


def quicksort(lst):
    print 'original list'
    return quicksort_helper(lst, 0, len(lst)-1)

print quicksort(['1.2.3', '4.11.6', '4.2.0', '1.5.19', '1.5.5', '4.1.3', '2.3.1',
                '10.5.5', '11.3.0'])

# print quicksort([2,4,3,5,1])

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





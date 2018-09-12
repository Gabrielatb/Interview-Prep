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
def quicksort(lst):

    if len(lst) < 2:
        return lst
    
    mid = len(lst)/2
    pivot = lst[mid]
    left, right, eq = [], [], []

    for elem in lst:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            eq.append(elem)

    return quicksort(left) + eq + quicksort(right)


# #merge sort lists
# def merge_sort(lst):


#     length = len(lst)

#     if length < 2:
#         return

#     mid = length/2
#     left = lst[:mid]
#     right = lst[mid:]


#     merge_sort(right)
#     merge_sort(left)
#     merge(left, right, lst)

#     return lst

# def merge(l, r, nums):


#     len_l = len(l)
#     len_r = len(r)
#     indx_r = 0
#     indx_l = 0
#     indx_nums = 0

#     while len_l > indx_l and len_r > indx_r:
#         if l[indx_l] > r[indx_r]:
#             nums[indx_nums] = r[indx_r]
#             indx_r +=1

#         else:
#             nums[indx_nums] = l[indx_l]
#             indx_l +=1

#         indx_nums += 1


#     while len_l > indx_l:
#         nums[indx_nums] = l[indx_l]
#         indx_l +=1
#         indx_nums += 1

#     while len_r > indx_r:
#         nums[indx_nums] = r[indx_r]
#         indx_r +=1
#         indx_nums += 1

#     print nums

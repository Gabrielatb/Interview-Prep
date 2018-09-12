# #merge sort implementation from my code school



def mergesort(a):

    n = len(a)
    left = []
    right = []

    if n < 2:
        return 


    for i in range(0,n):
        if i < n /2:
            left.append(a[i])
        else:
            right.append(a[i])

    mergesort(left)
    mergesort(right)
    merge(left, right, a)
    return a

def merge(l, r, nums):

    len_l = len(l)
    len_r = len(r)
    i = 0
    j = 0
    k = 0

    while len_l > i and len_r > j:
        if l[i] > r[j]:
            nums[k] = r[j]
            j += 1

        elif l[i] < r[j]:
            nums[k] = l[i]
            i += 1

        k += 1

    while len_l > i:
        nums[k] = l[i]
        i += 1
        k += 1

    while len_r > j:
        nums[k] = r[j]
        j += 1
        k += 1


# class MergeSort:

    # def _sort(self, arr):
    #     arr1 = []
    #     arr2 = []

    #     n = len(arr)

    #     if n <= 1:
    #         return

    #     for i in range(0, n):
    #         if i < (n / 2):
    #             arr1.append(arr[i])
    #         else:
    #             arr2.append(arr[i])

    #     self._sort(arr1)
    #     self._sort(arr2)
    #     self._merge(arr, arr1, arr2)
    #     return arr

    # def _merge(self, arr, arr1, arr2):  
    #     end1 = len(arr1)
    #     end2 = len(arr2)
    #     start1 = 0
    #     start2 = 0
    #     k = 0

    #     while (start1 < end1) and (start2 < end2):
    #         if arr1[start1] < arr2[start2]:
    #             arr[k] = arr1[start1]
    #             start1 += 1
    #         else:
    #             arr[k] = arr2[start2]
    #             start2 += 1
    #         k += 1

    #     while start1 < end1:
    #         arr[k] = arr1[start1]
    #         start1 += 1
    #         k += 1

    #     while start2 < end2:
    #         arr[k] = arr2[start2]
    #         start2 += 1
    #         k += 1


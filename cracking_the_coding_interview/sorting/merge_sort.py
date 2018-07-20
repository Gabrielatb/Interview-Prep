#generic merge sort 



def merge_sort(lst):


    if len(lst) < 2:
        return lst

    mid = len(lst)/ 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):

    result = []

    while left or right:

        if left == []:
            result.append(right.pop(0))

        elif right == []:
            result.append(left.pop(0))

        elif left[0] < right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))

    
    return result






print merge_sort([4,7,3,9,0,22,])


#Runtime: O(nlogn)


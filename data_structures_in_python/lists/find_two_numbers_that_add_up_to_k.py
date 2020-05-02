# Given a list and a number "k", find two numbers from the list that sum to "k".

# Sample Input
# lst = [1,21,3,14,5,60,7,6]
# k = 81
# Sample Output
# lst = [21,60]


#######################
# BINARY SEARCH
#######################

# space: O(1)
# runTime: O(nlogn)
def binarySearch(lst, target):
    print (lst, target)
    indx1 = 0
    indx2 = len(lst) - 1
    found = False
    while indx1 <= indx2 and not found:
        mid = (indx1 + indx2) // 2
        if target < lst[mid]:
            indx2 = mid - 1
        elif target > lst[mid]:
            indx1 = mid + 1
        else:
            found = True
    if found:
        return lst[mid]
    return False

def findSum(lst, k):
    lst.sort()
    for indx in range(len(lst)):
        target = k - lst[indx]
        result = binarySearch(lst, target)
        if type(result) is not bool:
            return [lst[indx], result]
    return False

#############################
# MOVING INDICES
##############################
# space: O(1)
# runTime: O(nlogn)
def findSum(lst, k):
    lst.sort()
    indx1 = 0
    indx2 = len(lst) - 1
    while indx1 != indx2:
        num_sum  = lst[indx1] + lst[indx2]
        if num_sum < k:
            indx1 += 1
        elif num_sum > k:
            indx1 -= 1
        else:
            return [lst[indx1], lst[indx2]]

print(findSum([1,21,3,14,5,60,7,6], 81))



################################
# Using collections
################################
# space: O(n)
# time: O(n)
import collections

def findFirstUnique(lst):
    appearance_count = collections.OrderedDict()
    for num in lst:
        if num in appearance_count:
            appearance_count[num] += 1
        else:
            appearance_count[num] = 1
    for num in appearance_count:
        if appearance_count[num] == 1:
            return num
    return None

print(findFirstUnique([9, 2, 3, 2, 6, 6]))
print(findFirstUnique([4, 5, 1, 2, 0, 4]))
################################
# Brute Force 
################################
# space: O(1)
# time: O(n^2)
def findFirstUnique(lst):
    for indx in range(len(lst)):
        isRepeating = False
        for j in range(indx + 1, len(lst)):
            if lst[indx] == lst[j]:
                isRepeating = True
                break
        if isRepeating is not True:
            return lst[indx]
    return False

print(findFirstUnique([9, 2, 3, 2, 6, 6]))
print(findFirstUnique([4, 5, 1, 2, 0, 4]))

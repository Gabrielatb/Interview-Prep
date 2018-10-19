#invariant

#Design an algorithm, takes as input an array and a number
#determines if there are three entries in the array
#which add to a specified number. You are able to use an entry 
#more than once

def has_two_sum(A, t):

    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False

def has_three_sum(nums, t):

    nums.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    for num in nums:
        if has_two_sum(nums, t-num):
            return True
    return False


print has_three_sum([11,2,5,7,3], 21)
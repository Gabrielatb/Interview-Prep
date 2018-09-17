# Given a list of unordered integers, find the eqilibrium point where the
# sum of all ints to the left equals the sum of all ints to the right.
# Notes:
#     - Return the index of the equilibrium
#     - If there is no exact equilibrium point, return the closest


# [ 5,8,10, 23, 0 ]


    # difference variable

    # iterate through my list enumerate (left, right)

    # left= [:i]

    #iterate get sum

    #right = [i+1:]

    #iterate and get sum

    #take difference of sum

    # if difference is lower, then save to variable

# O(n**2)

# O(1)

def find_eq1(lst):

    min_diff = None
    indx = 0

    total_right = 0

    for i, num in enumerate(lst):

        total_right += num

        total_left = sum(lst[i+1:])

        diff = abs(total_left - total_right)

        if min_diff is None or diff < min_diff:
            min_diff = diff
            indx = i

    return indx





def find_eq2(lst):

    r_indx, l_indx = len(lst) -1, 0

    r_sum, l_sum = lst[r_sum], lst[l_sum]


    while l_indx < r_indx:
        if l_sum < r_sum:

            l_indx += 1
            l_sum += lst[l_indx]


        else:
            r_indx -= 1
            r_sum += lst[r_indx]
    return left

print find_eq1([2, 4, 4, 1, 2, 1, 5])






# Given a list of tuples that each represent a link,
# determine whether they can form a linked list.


# ex:
# [(1,2), (2,3), (3,4)] => True, 1 -> 2 -> 3 -> 4

# [(1,2), (3,4), (4,5)] => False, 1 -> 2   3 -> 4 -> 5

# [(1,2), (2,3), (2,4)] => False, branching

# [(1,2), (2,3), (3,1)] => False, loop


def is_ll(lst):
    """Return True if list of tuples represents link"""


    #iterate through my list 

    #First check if first elem in first tuple is diff than last element in last tuple

    #check to see that the last elem in tuple is same as first element in next tuple

    # return True
    if lst[0][0] == lst[-1][-1]:
        return False
    else:
        for i in range(len(lst)-1):
            if lst[i][-1] != lst[i+1][0]:
                return False
    return True 



print is_ll([(1,2), (2,3), (3,4)])
print is_ll([(1,2), (3,4), (4,5)])
print is_ll([(1,2), (2,3), (2,4)])
print is_ll([(1,2), (2,3), (3,1)])
#Design an algorithm that takes as input a set of tasks
#and returns an optimum assignment


# ex. 5,2,1,6,4,4


# Time: O(n log n)
# Space O(n)
def optimum_assignment(lst):

    lst.sort()
    return_lst = []
    for _ in range(len(lst)/2):
        max_, min_ = lst[0], lst[-1]
        lst = lst[1:-1]
        return_lst.append((max_, min_))
    return return_lst


print optimum_assignment([5,2,1,6,4,4])
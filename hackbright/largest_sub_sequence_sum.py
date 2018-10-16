def largest_sum(nums):
    """
        >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
        [4, -2, 3]

        >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
        [4, -2, 3]

        >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
        [19]

        >>> largest_sum([2, 2, -10, 1, 3, -20])
        [2, 2]

        >>> largest_sum([2, -2, 3, -1])
        [3]

        >>> largest_sum([-1, -2])
        []

    """
#################################################################################
# Time Complexity O(N)
# Space Complexity O(1)

    # curr_sum_start = 0
    # curr_sum = 0


    # max_sum_start = 0
    # max_sum_end = -1
    # max_sum = 0

    # for i, num in enumerate(nums):
    #     curr_sum += num
    #     if max_sum < curr_sum:
    #         max_sum = curr_sum
    #         max_sum_start = curr_sum_start
    #         max_sum_end = i
    #     if curr_sum <= 0:
    #         # print i
    #         curr_sum = 0
    #         curr_sum_start = i +1
       

    # return nums[max_sum_start:max_sum_end+1]

# print largest_sum([2, 2, -10, 1, 3, -20])
# # print largest_sum([-1, -2])
# print largest_sum([2, -2, 3, -1])
    

################################################################################
#Time Complexity: O(n**2)
#Space Complexity O(n)

    # max_sum_lst = []
    # max_sum = 0

    # max_so_far_lst = []
    # max_so_far = 0

    # for num in nums:
    #     max_sum += num
    #     max_sum_lst.append(num)
    #     if max_so_far < max_sum:
    #         max_so_far = max_sum
    #         max_so_far_lst = max_sum_lst[::]
    #     elif max_sum <= 0:
    #         max_sum = 0
    #         max_sum_lst = [] 

    # return max_so_far_lst
################################################################################

#Recursively
# def largest_sum(nums):

# >>> largest_sum([2, -2, 3, -1])
#         [3]






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ' ****** ALL TESTS PASSED ****** '
# https://fellowship.hackbrightacademy.com/materials/challenges/largest-sum/solution/index.html#largest-sum-solution
    
# https://en.wikipedia.org/wiki/Greedy_algorithm
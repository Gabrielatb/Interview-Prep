def largest_sum(nums):
    # """
    #     >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    #     [4, -2, 3]

    #     >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    #     [4, -2, 3]

    #     >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    #     [19]

    #     >>> largest_sum([2, 2, -10, 1, 3, -20])
    #     [2, 2]

    #     >>> largest_sum([2, -2, 3, -1])
    #     [3]

    #     >>> largest_sum([-1, -2])
    #     []

    # """

    #[2, -2, 3, -1]

    for num in nums:
        print num


print largest_sum([1, 0, 3, -8, 4, -2, 3])











    #start, end = index
    # max_seq_so_far = [0, 0]
    # max_so_far = 0
    
#start, end = index
    # max_seq = [0, 0]
    # max_sum = 0
    
    # for i, n in enumerate(nums):
        
    #     max_sum = max_sum + n
    #     #increment j
    #     max_seq.append(n)
        
    #     if max_so_far < max_sum:
    #         max_so_far = max_sum
    #         max_seq_so_far = max_seq[:]
            
    #     if max_sum <= 0:
    #         max_sum = 0
    #         max_seq = (i,i)
            
    # return max_seq_so_far
    
    
import doctest
doctest.testmod()
# https://fellowship.hackbrightacademy.com/materials/challenges/largest-sum/solution/index.html#largest-sum-solution
    
# https://en.wikipedia.org/wiki/Greedy_algorithm
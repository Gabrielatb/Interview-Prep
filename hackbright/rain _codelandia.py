"""

The first example:

>>> rain([2, 5, 2, 3, 4, 1])
3


No buildings mean no rain is captured:

>>> rain([])
0

All-same height buildings capture no rain:

>>> rain([10])
0

>>> rain([10, 10])
0

>>> rain([10, 10, 10, 10])
0

If there’s nothing between taller buildings, no rain is captured:

>>> rain([2, 3, 10])
0

>>> rain([10, 3, 2])
0

If two tallest buildings are same height and on ends, it’s easy:

>>> rain([10, 5, 10])
5

>>> rain([10, 2, 3, 4, 10])
21

>>> rain([10, 4, 3, 2, 10])
21

>>> rain([10, 2, 4, 3, 10])
21

If two tallest buildings are ends, but not the same height, it will fall off the shorter of the two:

>>> rain([10, 2, 3, 4, 9])
18

Rain falls off the left and right edges:

>>> rain([2, 3, 10, 5, 5, 10, 3, 2])
10

Trickier:

>>> rain([3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
15

. = water, _ = rooftop, | = wall.

10        ___.___
9         | |.| |
8         | |.| |
7         | |_| |
6         |     |. . .___
5   ___. .|     |__. .| |.___
4   | |__.|       |__.| |.| |
3 __|   |_|         |_| |.| |
2 |                     |_| |__
1 |                           |
0 |                           |

       1 2   3   1 2 3   3
       \ /       \ /
        3    3    3  3   3 -- 5*3 == 15


A new one by me:

>>> rain([3, 5, 4, 3, 10, 7, 8, 7, 10, 5, 4, 3, 6, 2, 5, 2])
20

. = water, _ = rooftop, | = wall.

10        ___. . .___
9         | |. . .| |
8         | |.___.| |
7         | |_| |_| |
6         |         |. . .___ 
5   ___. .|         |__. .| |.___
4   | |__.|  3 2 3    |__.| |.| |
3 __|   |_|  | \ /      |_| |.| |
2 |          |  5 more      |_| |__
1 |           \ /                 |
0 |            8                  |

        
Subsequences:

3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2
   -----------
            ---------
                   --------------
                                -------

    
3, 5, 4, 3, 10, 7, 8, 7, 10, 5, 4, 3, 6, 2, 5, 2

                2  2  2
                1     1
"""



# [3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2]

#rain([10, 5, 10])

#count = 5
#left_building = 10
#right_building = 10
# Time: O(n)
# Space: O(n)
def rain(nums):
    count = 0
    left_building = 0
    right_building = 0
    right_building_lst = [0] * len(nums)
    
    
    for i in reversed(range(len(nums))):
        if nums[i] > right_building:
            right_building = nums[i]
            
        right_building_lst[i] = right_building
        
    for i, num in enumerate(nums):
        if num > left_building:
            left_building = num
        
        min_ = min(right_building_lst[i], left_building)
        if min_ - num > 0:
            count += min_ - num
        
    return count 

    



if __name__ == "__main__":
    quicktest = False
    if quicktest:
        print rain([10, 5, 10])
    else:
        import doctest
        results = doctest.testmod()
        if results.failed == 0:
            num_passed = (results.attempted - results.failed)
            doctest.master.summarize(True)
            print "\n*** ALL %d TESTS PASSED!\n" % num_passed
#8.4

#Write a method to return all subsets of a set


#given set of distinct int, return all subsets
#if given [1,2,3]

#return 
#[1], [2], [3], [1,2,3], [1,3], [2,3], [1,2] 



# I know I have to go from returning full list, to length of list as two, to length of list as 1,
# to empty list

def dfs(nums, subset, result):
    print "this is my nums ", nums
    print "this is my initial subset ", subset
    if len(nums) == 0:
        print "######################"
        return 

    for indx, num in enumerate(nums):
        result.append(subset + [num])
        print "this is my num ", num
        print "this is my result ", result
        print "this is my subset ", subset + [num]
        print "########################################"
        dfs(nums[indx+1:], subset + [num], result)
        
def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    result = [[]]

    dfs(nums, [], result) 
    return result




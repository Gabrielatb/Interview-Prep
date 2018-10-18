#generate powerset

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

#Time Complexity O(n2**n)
#Space Complexity O(n2**n)
def generate_power_set(nums):

    def directed_power_set(to_be_selected, subset):
        #BASE CASE: if indx exceeds indx of list, return 
        if to_be_selected == len(nums):
            #appending viable subset
          
            power_set.append(list(subset))
            return 



        #leaving subset as is 
        directed_power_set(to_be_selected + 1, subset)

        #generating the subset
        directed_power_set(to_be_selected+1, subset + [nums[to_be_selected]])


    power_set = []
    directed_power_set(0, [])
    return power_set



print generate_power_set([1,2])



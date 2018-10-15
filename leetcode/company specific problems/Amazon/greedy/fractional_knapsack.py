# Input:
#   Items as (value, weight) pairs
#   arr[] = [[60, 10], [100, 20], [120, 30]]
#   Knapsack Capacity, W = 50;
# Output:
#   Maximum possible value = 220
#   by taking items of weight 20 and 30 kg 


# Time: O(nlogn)
# Space: O(1)

def knapsack(lst, W):
    lst.sort(key=lambda x:x[0], reverse=True)
    
    value = 0
    for item in lst:
        if W - item[1] == 0:
            value += item[0]
            break
        elif item[1] <= W:
            W -= item[1]
            value += item[0]
    return value



print knapsack([[60, 10], [100, 30], [120, 30]], 50)
































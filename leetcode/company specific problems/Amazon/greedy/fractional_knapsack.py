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

    
    val = 0
    for tup in lst:
        if tup[1] <= W:
            val += tup[0]
             W -= tup[1]
        else:
            return val
    return val


print knapsack([[60, 10], [100, 20], [120, 30]], 50)
































































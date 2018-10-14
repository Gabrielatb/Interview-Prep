# Input:
#   Items as (value, weight) pairs
#   arr[] = [[60, 10], [100, 20], [120, 30]]
#   Knapsack Capacity, W = 50;
# Output:
#   Maximum possible value = 220
#   by taking items of weight 20 and 30 kg 

def fractional_knapsack(lst, W):
    lst.sort(key=lambda x:x[0])
    lst = lst[::-1]
  
    val = 0
    for item in lst:

        if item[1] <= W:
            print item
            W -= item[1]
            val += item[0]
    return val




print fractional_knapsack([[60, 10], [100, 20], [120, 30]], 50)
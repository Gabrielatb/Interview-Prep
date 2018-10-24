#input: [[-4,-1], [0,2], [3,6], [7,9], [11, 12], [14,17]]
#added interval is: [1,8]






def merge_intervals(lst, single_interval):
    #sort intervals by start time
    lst.append(single_interval)
    lst.sort(key=lambda x:x[0])
    merged = []
    for interval in lst:
        #if interval list is empty or if curr interval does not overlap with previous
        if merged == [] or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            #there is overlap so need to merge
            merged[-1][-1] = max(merged[-1][-1], interval[1])
    return merged




#add an interval to disjoint intervals

print merge_intervals([[-4,-1], [0,2], [3,6], [7,9], [11,12], [14,17]], [1,8])
#output [[-4,-1], [0,9], [11,12], [14,17]]

#assuming list is already sorted 
def add_interval(lst, single_interval):

  
    lst = merge_intervals(lst)
    append_indx = 0
    for indx, interval in enumerate(lst):

        #single interval does intersect with interval
        if interval[1] > single_interval[0]:
            append_indx = indx
            new_interval = [min(interval[0], single_interval[0]), max(interval[1], interval[1])]
          
    lst.insert(append_indx, lst)
    return lst








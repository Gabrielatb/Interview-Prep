#input: [[-4,-1], [0,2], [3,6], [7,9], [11, 12], [14,17]]
#added interval is: [1,8]






def merge_intervalS(lst):
    #sort intervals by start time
    sorted_intervals = lst.sort(key=lambda x:x[0])
    merged = []
    for interval in sorted_intervals:
        #if interval list is empty or if curr interval does not overlap with previous
        if merged == [] or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            #there is overlap so need to merge
            merged[-1][-1] = max(merged[-1][-1], interval[1])
    return merged


print merge_intervalS([[1,3], [2,6], [8,10], [15,18]])
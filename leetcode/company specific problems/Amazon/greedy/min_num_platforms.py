# Given arrival and departure times of all trains that reach a railway station,
#find the minimum number of platforms required for the railway station so that
#no train waits. We are given two arrays which represent arrival and departure times
#of trains that stop

# Input:  arr[]  = [9:00,  9:40, 9:50,  11:00, 15:00, 18:00]
#         dep[]  = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]
# Output: 3
# There are at-most three trains at a time (time between 11:00 to 11:20)


def min_number_platform(arr, dep):
    #sort lists by arrival time
    sorted_tuple_by_start_time = zip(*sorted(zip(arr, dep)))
    
    depart_indx = 0
    count = 1
    max_count = 0

    for start_indx in range(1, len(arr)):
        if arr[start_indx] < dep[depart_indx]:
            count +=1
            depart_indx = start_indx

        else:
            max_count = max(max_count, count)
            count = 0
        start_indx +=1

    max_count = max(max_count, count)
    return max_count



print min_number_platform([940, 950,  1100, 1500, 1800, 900],[1200, 1120, 1130, 1900, 2000,910])
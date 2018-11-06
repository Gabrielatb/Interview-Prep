 # Activity Selection problem

# You are given n activities with their start and finish times.
# Select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.


#  Time: O(nlogn)
# # Space: O(1)



def activity_selection(start, finish):

    f, s = zip(*sorted(zip(finish, start)))

    finish_time = 0
    count = 1
    for start_time in range(1, len(s)):
        if f[finish_time] <= s[start_time]:
            count += 1
            finish_time = start_time
    return count






# s = [20, 12, 10]
# f = [30, 25, 20]


s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9] 
print activity_selection(s,f)






















#[ (10, 20), (12, 25),(20, 30)]

    # start, finish = zip(*sorted(zip(finish, start)))
    
    # count = 1
    # f = 0
    # for s in range(1, len(start)):
    #     if start[s] >= finish[f]:
    #         count +=1
    #         f = s
    # return count







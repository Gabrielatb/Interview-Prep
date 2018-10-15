 # Activity Selection problem

# You are given n activities with their start and finish times.
# Select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.



# Time: O(nlogn)
# Space: O(1)

def max_activities(s, f):
    f,s = zip(*sorted(zip(f,s)))
    #tuples

    count = 1
    indx = 0
    for start in range(len(s)):
        if s[start] >= f[indx]:
            indx = start
            count +=1
    return count






s = [20, 12, 10]
f = [30, 25, 20]


# s = [1 , 3 , 0 , 5 , 8 , 5]
# f = [2 , 4 , 6 , 7 , 9 , 9] 
print max_activities(s,f)



















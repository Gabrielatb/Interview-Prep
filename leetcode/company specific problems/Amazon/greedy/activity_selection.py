 # Activity Selection problem

# You are given n activities with their start and finish times.
# Select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.
def unsorted(s, f):
    pass
  
def activity_selection(s , f ): 
    f,s = zip(*sorted(zip(f, s)))
 
    count = 1
    i = 0

    for j in range(len(f)):
        if s[j] >= f[i]:
            count +=1
            i=j
    return count



s = [20, 25, 10]
f = [30, 25, 20]


# s = [1 , 3 , 0 , 5 , 8 , 5] 
# f = [2 , 4 , 6 , 7 , 9 , 9] 
print activity_selection(s, f)




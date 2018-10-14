# Given an array of jobs where every job has a deadline and associated profit 
# if the job is finished before the deadline. It is also given that every job takes 
# single unit of time, so the minimum possible deadline for any job is 1. 
# How to maximize total profit if only one job can be scheduled at a time.

def job_seq(lst):

    profit_lst = [0] * len(lst)

    lst.sort(key=lambda x:x[2])
    lst = lst[::-1]
    
    # if profit_lst[0] == 0:
    #     profit_lst[0] = lst[0][0]
    #     print profit_lst
    
    for job in lst:
        if profit_lst[job[1]-1] == 0:
            profit_lst[job[1]-1] = job[0]
        else:
            i = job[1]-1
            while i >=0:
                if profit_lst[i] == 0:
                    profit_lst[i] = job[0]
                    break
                i-=1
    
    result_lst = []
    for job in profit_lst:
        if job != 0:
            result_lst.append(job)
    return result_lst   



lst = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], 
                   ['d', 1, 25], ['e', 3, 15]]
print job_seq(lst)
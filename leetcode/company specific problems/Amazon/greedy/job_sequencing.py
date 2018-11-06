# Given an array of jobs where every job has a deadline and associated profit 
# if the job is finished before the deadline. It is also given that every job takes 
# single unit of time, so the minimum possible deadline for any job is 1. 
# How to maximize total profit if only one job can be scheduled at a time.

#Time: O(n**2)
#Space: O(n)



def job_sequencing(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)
    key_holder_lst = [0] * len(jobs)

    for single_job in jobs:
        indx = single_job[1]-1
        while indx >= 0:
            if key_holder_lst[indx] == 0:
                key_holder_lst[indx] = single_job[0]
                break
            else:
                indx -=1

    return_lst = [x for x in key_holder_lst if x != 0]
    return return_lst


       
arr = [['a', 4, 20], 
       ['b', 1, 10],
       ['c', 1, 40], 
       ['d', 1, 30]]

print job_sequencing(arr)

















# def job_seq(jobs):
#     jobs.sort(key=lambda x:x[2])
#     jobs = jobs[::-1]

#     job_lst = [0] * len(jobs)

#     for job in jobs:
#         if job_lst[job[1]-1] == 0:
#             job_lst[job[1]-1] = job[0]
#         else:
#             job_interval = job[1] - 2
#             while job_interval >= 0:
#                 if job_lst[job_interval] == 0:
#                     job_lst[job_interval] == job[0]
#                     break
#                 else:
#                     job_interval -= 1
#     return_lst = []
#     for job in job_lst:
#         if job != 0:
#             return_lst.append(job)
#     return return_lst


# jobs = [['a', 4, 20], ['b', 1, 10], ['c', 1, 40], ['d', 1, 30]]


# print job_seq(jobs)














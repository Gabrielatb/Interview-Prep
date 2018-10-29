# Given n tasks with arrival time, priority and number of time units they need. 
# We need to schedule these tasks on a single resource. 
# The objective is to arrange tasks such that maximum priority tasks are taken.
# Objective is to minimize sum of product of priority and left time of tasks that are not scheduled due to limited time.
# This criteria simply means that the scheduling should cause minimum possible loss.

# Examples:

# Input : Total time = 3
#         Task1: arrival = 1, units = 2, priority = 300
#         Task2: arrival = 2, units = 2, priority = 100
# Output : 100

# Input : Total Time = 3
#         Task1: arrival = 1, units = 1, priority = 100
#         Task2: arrival = 2, units = 2, priority = 300
# Output : 0
def minLoss(lst):
    #priority queue

    #loss = sum of all priorty 

    #when one priority is done subtract from loss

    #sort tasks according to arrival time



n = 2
total_time = 3
arrival = [1, 2]
units = [2, 2]
priority = [100, 300]
  
print minLoss(n, t, arriv, units, priority)
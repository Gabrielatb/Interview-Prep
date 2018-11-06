# Given a char array representing tasks CPU need to do. 

# It contains capital letters A to Z where different letters represent
# different tasks.

# Tasks could be done without original order. 
# Each task could be done in one interval. For each interval, CPU could finish one
# task or just be idle.

# However, there is a non-negative cooling interval n that means between two same
# tasks, there must be at least n intervals that CPU are doing different tasks
# or just be idle.

# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.

# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 
# Number of instances equivalent to numbr of time tasks
# appears in the array


import heapq
import collections


def least_interval(tasks, n):

    if n == 0:
        return len(tasks)

    dictionary_count = collections.defaultdict(int)

    for task in tasks:
        dictionary_count[task] += 1


    total_count = 0
    cycle = n + 1

    #max heap
    heap = []
    for val in dictionary_count.values():
        if val > 0:
            heapq.heappush(heap, (-val))


    while heap:
        worktime=0
        temp = []
        for i in range(cycle):
            if heap:
                temp.append(heapq.heappop(heap))
                worktime +=1

        for count in temp:
            count *= -1
            count -=1
            if count > 0:
                heapq.heappush(heap, (-count))
        
        total_count += cycle if len(heap) > 0 else worktime
    return total_count







tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print least_interval(tasks, 2)









# def least_interval(taks, n):
#     table = {} 
#     for task in tasks:
#         table[task] = table.get(task, 0) + 1
    
#     idles = 0
#     while table:
#         length = len(table)
        


# tasks = ["A","A","A","B","B","B"]
# n = 2
# print least_interval(tasks, n)
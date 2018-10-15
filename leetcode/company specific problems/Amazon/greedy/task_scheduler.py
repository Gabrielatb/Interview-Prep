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


def least_interval(taks, n):
    table = {} 
    for task in tasks:
        table[task] = table.get(task, 0) + 1
    
    idles = 0
    while table:
        length = len(table)
        


tasks = ["A","A","A","B","B","B"]
n = 2
print least_interval(tasks, n)
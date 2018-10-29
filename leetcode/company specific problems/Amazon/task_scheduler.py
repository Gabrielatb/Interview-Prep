# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters representdifferent tasks.
# Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same
# tasks, there must be at least n intervals that CPU are doing different tasks
# or just be idle.

# You need to return the least number of intervals the CPU will take
# to finish all the given tasks.
 
# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.



#heapify after n 
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        if n == 0:
            return len(tasks)

        


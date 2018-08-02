# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count1 = 0
        count2 = 0
        multiplier = 1
        
        while l1:
            count1 += multiplier * l1.val
            l1 = l1.next
            multiplier *= 10
            
        multiplier = 1    
        while l2:
            count2 += multiplier * l2.val
            l2 = l2.next
            multiplier *= 10
            
        final_count = count1 + count2
        fc_string = str(final_count)

        
        prev = None
        for num in fc_string:
            print num
            num = int(num)
            new_node = ListNode(num)
            new_node.next = prev
            prev = new_node
            
        return prev
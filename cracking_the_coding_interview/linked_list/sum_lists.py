#problem also on Leetcode:

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

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
        mult1 = 1
        
        while l1:
            if mult1 == 1:
                count1 += l1.val
            else:
                count1 += l1.val * mult1
            mult1 = mult1 * 10
            l1 = l1.next    
        print "count: " + str(count1)
                
       
            
            
        count2 = 0
        mult2 = 1
        
        while l2:
            if mult2 == 1:
                count2 += l2.val
            else:
                count2 += l2.val * mult2
            mult2 = mult2 * 10
            l2 = l2.next
                
        print "count: " + str(count2)
                
            
            
        final_count = count1 + count2
        final_count = str(final_count)
        
        prev = None
        for num in final_count:
            new_node = ListNode(num)
            new_node.next = prev
            prev = new_node
            
        return prev
            
            
            

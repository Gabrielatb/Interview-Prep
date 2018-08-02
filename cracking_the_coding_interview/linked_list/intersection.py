#problem number 2.7


#Also leetcode problem

# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.



# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        len_A = 0
        len_B = 0
        currA = headA
        currB = headB
        
        while currA:
            currA = currA.next
            len_A +=1
            
        while currB:
            currB = currB.next
            len_B +=1
            
        if len_B > len_A:
            diff = len_B - len_A
            for _ in range(diff):
                headB = headB.next
                
        elif len_A > len_B:
            diff = len_A - len_B
            for _ in range(diff):
                headA = headA.next
            
                
                
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None
        
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        num_1_list = []
        num_2_list = []
        count1 = 0
        count2 = 0
        
        while l1:
            num_1_list.append(l1.val)
            l1 = l1.next
            
        while l2:
            num_2_list.append(l2.val)
            l2 = l2.next
        
        len1 = len(num_1_list)
        for i in range(len(num_1_list)):
            len1 -= 1
            if len1 == 0:
                count1 += num_1_list[i]
            else:
                count1 += num_1_list[i] * 10**len1
        print count1
            
        len2 = len(num_2_list)
        for i in range(len(num_2_list)):
            len2 -= 1
            if len2 == 0:
                count2 += num_2_list[i]
            else:
                count2 += num_2_list[i] * 10**len2
        print count2
            
        count = str(count1 + count2)
        prev = ListNode(0)
        head = prev
        for num in count:
            node = ListNode(int(num))
            prev.next = node
            prev = prev.next
        return head.next
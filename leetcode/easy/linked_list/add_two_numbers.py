# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1 = []
        list_2 = []
        
        while l1:
            list_1.insert(0, l1.val)
            l1 = l1.next     

        
        while l2:
            list_2.insert(0, l2.val)
            l2 = l2.next
        
        count1 = 0
        count2 = 0
        
        len1 = len(list_1)
        for num in list_1:
            len1 -= 1
            count1 += num * (10**len1)
            
        len2 = len(list_2)
        for num in list_2:
            len2 -= 1
            count2 += num * (10**len2)
            
        count3 = str(count2 + count1)
        count3 = list(count3)
                     
        
         #reverse list in place
   
        for i in range(len(count3)/2):
            temp = count3[-(i+1)]
            count3[-(i+1)] = count3[i]
            count3[i] = temp
        
        prev = ListNode(0)
        head = prev
        for num in count3:
            node = ListNode(int(num))
            prev.next = node
            prev = prev.next
        return head.next
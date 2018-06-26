# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    #***riginal solution***

    if len(lists) == 0:
        return None
    
    nums = []
    
    #iterating through list, grabbing single linked list, iterate through that link list, and putting it onto my newly created list
    
    for ll in lists:
        #have single link list, will iterate through it
        curr = ll
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
            
    sorted_nums = sorted(nums)
    
    if len(sorted_nums) == 0:
        return None
        
        #making a dummy head
        dummy = ListNode(nums)
        #linking first element in sorted_nums to dummynode
        curr =  ListNode(sorted_nums[0])
        dummy.next = curr
        
        for i in range(len(sorted_nums)):
            if i == 0:
                continue
            else:
                node = ListNode(sorted_nums[i])
                curr.next = node
                curr = node
                
        return dummy.next

    #***alternate, cleaner solution***
        nums = []

        for head in lists:
            current = head
            while current:
                nums.append(current.val)
                current = current.next

        sorted_list = sorted(nums)
        head = ListNode(0)
        current = head
        for num in sorted_list:
            current.next = ListNode(num)
            current = current.next

        return head.next

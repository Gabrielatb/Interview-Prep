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

    #create list to add all nodes of k linked list
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

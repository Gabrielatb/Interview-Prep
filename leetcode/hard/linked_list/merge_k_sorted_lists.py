# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkList(object):

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node


    def print_list(self):
        if self.head is None:
            print "there is nothing to print"

        else:
            curr = self.head
            while curr.next:
                print curr.val
                curr = curr.next

    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """

        #### BRUTE FORCE SOLUTION ####
        #Time complexity is NlognN because of sort
        #N or iterating through the entire list
        #N log N for sorting the list
        #N for creating new linked list

        #Space Complexity O(N) creating empty list
        #Sorting cost N
        #creating new linked list N
        # nums = []

        # for ll in lists:
        #     curr = ll.head

        #     while curr:
        #         nums.append(curr.val)
        #         curr = curr.next

        # nums.sort()
        # dummy = dummy_head = Node(0)
        # for num in nums:
        #     # print num
        #     dummy.next = Node(num)
        #     dummy = dummy.next


        # return dummy_head.next

        #########Cleaner Solution################

    ###Time Complexity: Nlogk where n is number of nodes in k link list
    ###Space complexity O(1)
        def mergeKLists(self, lst):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """

            length = len(lst)

            interval = 1

            while interval < length:
                for i in range(0, length-interval, interval*2):
                    lst[i] = self.merge2Lists(lst[i], lst[i+interval])

                interval *= 2

            return lst[0] if length > 0 else lst


        def Merge2Lists(self, l1, l2):

            dummy = dummy_head = Node(0)

            while l1 and l2:
                if l1.val >l2.val:
                    dummy.next = l2
                    l2 = l2.next
                    dummy = dummy.next

                elif l2.val >= l1.val:
                    dummy.next = l1
                    l1 = l1.next
                    dummy = dummy.next

            if l1:
                dummy.next = l1

            if l2:
                dummy.next = l2
            return dummy_head.next

      











if __name__ == '__main__':
    ll1 = LinkList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll2 = LinkList()
    ll2.append(5)
    ll2.append(6)
    ll2.append(7)
    ll2.append(8)
    ll3 = LinkList()
    ll3.append(9)
    ll3.append(10)
    ll3.append(11)
    ll3.append(12)

























# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#     #***riginal solution***

#     if len(lists) == 0:
#         return None
    
#     nums = []
    
#     #iterating through list, grabbing single linked list, iterate through that link list, and putting it onto my newly created list
    
#     for ll in lists:
#         #have single link list, will iterate through it
#         curr = ll
#         while curr:
#             nums.append(curr.val)
#             curr = curr.next
        
            
#     sorted_nums = sorted(nums)
    
#     if len(sorted_nums) == 0:
#         return None
        
#         #making a dummy head
#         dummy = ListNode(nums)
#         #linking first element in sorted_nums to dummynode
#         curr =  ListNode(sorted_nums[0])
#         dummy.next = curr
        
#         for i in range(len(sorted_nums)):
#             if i == 0:
#                 continue
#             else:
#                 node = ListNode(sorted_nums[i])
#                 curr.next = node
#                 curr = node
                
#         return dummy.next

#     #***alternate, cleaner solution***
#         nums = []

#         for head in lists:
#             current = head
#             while current:
#                 nums.append(current.val)
#                 current = current.next

#         sorted_list = sorted(nums)
#         head = ListNode(0)
#         current = head
#         for num in sorted_list:
#             current.next = ListNode(num)
#             current = current.next

#         return head.next

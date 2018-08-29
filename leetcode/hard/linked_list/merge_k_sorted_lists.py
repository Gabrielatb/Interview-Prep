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
    def merge(self, ll1, ll2):
        dummy = dummy_head = ListNode(0)
        
        while ll1 and ll2:
            if ll1.val > ll2.val:
                dummy.next = ll2
                dummy = dummy.next
                ll2 = ll2.next
            else:
                dummy.next = ll1
                dummy = dummy.next
                ll1 = ll1.next
        
        if ll1:
            dummy.next = ll1
        if ll2:
            dummy.next = ll2
            
        return dummy_head.next
    
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            for ll in lists:
                return ll
            
        mid = len(lists)/2
        
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        
            
            
        return self.merge(left, right)
        
        
        
        











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


























# Merge two sorted linked lists and return it as a new list.
#The new list should be made by splicing together the nodes of the first two lists.


# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next:
                print curr
                curr = curr.next

            curr.next = new_node


    def print_list(self):

        if self.head is None:
            print "There is nothing to print"
        else:
            curr = self.head
            while curr:
                print curr.data
                curr = curr.next


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        dummy_head = dummy = Node(0)
        curr1 = l1.head
        curr2 = l2.head
        
        while curr1 is not None and curr2 is not None:
            if curr2.data < curr1.data:
                temp = curr2.next
                dummy.next = curr2
                curr2.next = None
                curr2 = temp
                dummy = dummy.next
                print dummy.data

            else:
                temp = curr1.next
                dummy.next = curr1
                curr1.next = None
                curr1 = temp
                dummy = dummy.next
                print dummy.data
        if curr1 is None and curr2 is None:

            return dummy_head.next

        elif curr1 is None:
            dummy.next = curr2

        elif curr2 is None:
            dummy.next = curr1

        return dummy_head.next




if __name__ == "__main__":


    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)

    l2.append(1)
    l2.append(3)
    l2.append(4)



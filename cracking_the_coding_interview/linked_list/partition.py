#write code to partition a linked list around a value, all nodes less than value 
#come before all nodes greater than or equal to the value


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node
        self.tail = new_node

#1 -> 5 -> 9 -> 2 -> 7 -> 3 -> None
    def print_list(self):
        curr = self.head

        while curr:
            print curr.val
            curr = curr.next


    def partition(self, x):

        #O(n) time complexity
        #O(1) space complexity
    
        curr = self.head
        dummy_head = head= ListNode(0)
        dummy_end = head_end = ListNode(0)

        while curr:
            if curr.val  < x:
                dummy_head.next = curr
                dummy_head = dummy_head.next
            else:
                dummy_end.next = curr
                dummy_end = dummy_end.next

            curr = curr.next

        dummy_end.next = None
        print dummy_head.val
        print head_end.next.val

        dummy_head.next = head_end.next
        self.head = head.next
        self.tail = dummy_end
        return head.next.val









if __name__ == '__main__':
    # ll = LinkedList()
    # ll.append(1)
    # ll.append(5) 
    # ll.append(9) 
    # ll.append(2) 
    # ll.append(7) 
    # ll.append(3)  

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(1)




























#Problem 2.6


#2 -> 4 ->5 ->4 ->2 ---> return True

# 1-> 2 -> 3 ----> return False

# 1 ----> return True


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
        new_node = self.tail



    def print_list(self):
        if self.head is None:
            return 'No nodes to print'

        curr = self.head
        while curr:
            print curr.data
            curr = curr.next

    
    def palindrome(self):

        #Time Complexity O(n)

        #Space Complexity O(1)

        #find middle node reverse second half of link list

        # if self.head is None or self.head.next is None:
        #     return True

        # #find middle node
        # slow = fast = self.head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # #reverse link list
        # prev = node
        # while slow:
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp

        # #compare first and second half
        # while prev and self.head:
        #     if prev.val != self.head.val:
        #         return False
        #     prev = prev.next
        #     self.head = self.head.next

        # return True



        #creating a stack

        curr = self.head
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr:
            node = stack.pop() 
            if node.val != curr.val:
                return False
            curr = curr.next

        return True

        #Time Complexity O(n)
        #Space Complexity O(n)





if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    # ll.append(4)
    # ll.append(5)
    ll.append(0)
    ll.append(1)
    # ll.append(2)

























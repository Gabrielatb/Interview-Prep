#Problem 2.6

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
        elif self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def print_list(self):

        curr = self.head
        while curr:
            print curr.val
            curr = curr.next

    def palindrome(self):
      
        if not self.head or not self.head.next:
            return None


        node_count = 0
        curr = self.head

        while curr:
            node_count +=1
            curr = curr.next
            
        curr = self.head
        prev = None
        for _ in range(node_count/2):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        
        if node_count % 2 !=0:
            curr = curr.next


        while prev:
            if prev.val == curr.val:
                curr = curr.next
                prev = prev.next
            else:
                return False

        return True



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(1)
    # ll.append(3)

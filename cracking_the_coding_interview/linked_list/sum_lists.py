# 7->1->6, 5->9->2

#617 + 295
#returning 9->1->2

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

    def print_list(self):
        if self.head is None:
            return None

        curr = self.head
        while curr:
            print curr.val

    def sum_list(self, ll1, ll2):
        
        counter = 1
        total = 0
        count1 = count2 = 0
        curr1, curr2 = ll1.head, ll2.head

        while curr1:

            count1 += (curr1.val) * counter
            counter *=10
            curr1 = curr1.next

        counter = 1    
        while curr2:

            count2 += (curr2.val) * counter
            counter *=10
            curr2 = curr2.next


        total = str(count1 + count2)
        prev = None

        for num in total:
            num = int(num)
            node = ListNode(num)
            node.next = prev
            prev = node

        return prev.val

#Time complexity O(max(m, n))
#Space Complexity O(max(m,n))




if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.append(7)
    ll1.append(1)
    ll1.append(6)

    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(2)








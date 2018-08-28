# return kth to last element of a singly linked list



#1 -> 2 -> 3 -> 4-> 5 -> 
#k = 3, return 3
#k = 4, return 2
#k =  2, return 4




class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

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
            print curr.data
            curr = curr.next


    def return_kth(self, root, k):
  

        #create two pointers that are k length from each other
        #when end pointer reaches end, return beg pointer
        end = self.head
        beg = self.head

        while k >1:
            k-=1
            end = end.next

        while end.next:
            end = end.next
            beg = beg.next
        return beg.data





        # length of the list
        # subtract from the length
        # create counter

        length = 0
        curr = self.head
        while curr:
            length +=1
            curr = curr.next
 
        count = length-k

        curr = self.head

        while count > 0:
            count -=1
            curr = curr.next


        return curr.data

        #time complexity O(n)
        #space complexity O(1)

    def delete_kth(self, root, k):
        dummy = ListNode(0)
        dummy.next = head
        end, beg = dummy, dummy

        for _ in range(n):
            end = end.next

        while end.next:
            end = end.next
            beg = beg.next


        beg.next = beg.next.next
        
        return dummy.next













if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)




























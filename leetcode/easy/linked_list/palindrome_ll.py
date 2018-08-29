# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true

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
        curr = self.head

        while curr:
            print curr.data
            curr = curr.next


    #Time Complexity: O(n)
    #Space Complexity O(1)
    def palindrome(self):
        if self.head is None:
            return None

        mid = self.head
        fast = self.head

        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next

        end = mid.next
        mid.next = None

        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp

        curr = self.head
        while prev and curr:
            if prev.data != curr.data:
                return False
            prev = prev.next
            curr = curr.next
        return True



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(1)





    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
        # """
        #O(n) space complexity
        #O(n) time complexity
        
        # stack = []
        # node = head
        # while node:
        #     stack.append(node)
        #     node = node.next
            
            
        # curr = head
        # while curr:
        #     node = stack.pop()
        #     if node.val != curr.val:
        #         return False
        #     curr = curr.next
            
        # return True


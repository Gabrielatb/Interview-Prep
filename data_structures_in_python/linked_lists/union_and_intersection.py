# The union function will take two linked lists and return their union.

# The intersection function will return all the elements that are common between two linked lists.

# Input #
# Two linked lists.

# Output #
# A list containing the union of the two lists.
# A list containing the intersection of the two lists.
# Sample Input #
# list1 = 10->20->80->60
# list2 = 15->20->30->60->45
# Sample Output #
# union = 10->20->80->60->15->30->45
# intersection = 20->60

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head == None:
            print("There is no List to print :)")
            return

        curr = self.head
        while curr.next:
            print(curr.data, end="->")
            curr = curr.next

        print(curr.data, end="->None")
        print(" ")
        return

    def remove_repeating_elements(self):
        seen = []
        curr = self.head
        prev = None
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.append(curr.data)
                prev = curr
            curr = curr.next
        return

    def remove_non_repeating_elements(self):
        seen = []
        curr = self.head
        new_list = None
        while curr:
            if curr.data in seen:
                if new_list == None:
                    self.head = curr
                    new_list = self.head
                else:
                    new_list.next = curr
                    new_list = curr
            else:
                seen.append(curr.data)
            curr = curr.next
        new_list.next = None
        return new_list

    def is_empty(self):
        if self.head == None:
            return True
        return False

# 10->20->80->60->15->20->30->60->45->None


ll_1 = LinkedList()
ll_2 = LinkedList()

# list1 = 10->20->80->60
# list2 = 15->20->30->60->45
num_list_1 = [60, 80, 20, 10]
num_list2 = [45, 60, 30, 20, 15]

# Sample Output #
# union = 10->20->80->60->15->30->45
# intersection = 20->60

for num in num_list_1:
    ll_1.add_node_at_head(num)
# ll_1.print_list()

for num in num_list2:
    ll_2.add_node_at_head(num)
# ll_2.print_list()


# O(m+n)^2
def union(ll_1, ll_2):
    if ll_1.is_empty():
        return ll_2
    elif ll_2.is_empty():
        return ll_1

    curr = ll_1.head
    while curr.next:
        curr = curr.next
    curr.next = ll_2.head
    ll_1.remove_repeating_elements()
    return ll_1
# max(O(mn),O(min(m,n)
# ​2
# ​​ ))
def intersection(ll_1, ll_2):
    curr = ll_1.head
    while curr.next:
        curr = curr.next
    curr.next = ll_2.head
    ll_1.remove_non_repeating_elements()
    return ll_1

# union_list = union(ll_1, ll_2)    
# union_list.print_list()

intersection_list = intersection(ll_1, ll_2)    
intersection_list.print_list()


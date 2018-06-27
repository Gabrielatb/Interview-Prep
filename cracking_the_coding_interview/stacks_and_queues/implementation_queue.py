#queue: first in first out FIFO

#list 
class Queue(object):

    #peek, length, empty, is empty, print

    def __init__(self, inlist):
        self.queue = list(inlist)


    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        else:
            self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def length(self):
        return len(self.queue)

    def empty(self):
        self.queue = []

    def is_empty(self):
        if self.queue == []:
            return True
        return False

    def print_queue(self):

        for elem in self.queue:
            print elem



#linked list 
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):

    #peek, length, empty, is empty, print

    def __init__(self, inlist):
        self.head = None
        self.tail = None
        self.length = len(inlist)

        prev = None
        for item in inlist[::-1]:
            curr = Node(item)
            if self.tail is None:
                self.tail = curr
            curr.next = prev
            prev = curr

        self.head = prev


    def enqueue(self, item):

        node = Node(item)
        self.length += 1
        if self.is_empty():
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node


    def dequeue(self):
        if self.is_empty():
            return None

        else:
            self.length -= 1
            curr = self.head.next
            self.head.next = None
            self.head = curr



    def peek(self):
        return self.head.data

    def length(self):
        return self.length

    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True

        return False

    def print_queue(self):

        curr = self.head
        while curr.next:
            print curr.data
            curr = curr.next







if __name__ == "__main__":

    animals = Queue(['dog', 'cat', 'butterfly'])







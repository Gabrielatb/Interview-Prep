###3.2###

#how could you design a stack which in addition to push, pop has function which returns
# min element. Push, pop and min should all operate on O(1)

#stack is first in firs out FIFO

class Stack(object):
    
    def __init__(self):
        self.stack = []
        self.min_elem = []

    def push(self, item):
        if self.min_elem == []:
            self.min_elem.append(item)
        elif item < self.min_elem[-1]:
            self.min_elem.append(item)

        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            item = self.stack.pop()
            if self.min_elem[-1] == item:
                self.min_elem.pop()

    def min_element(self):
        return self.min_elem[-1]


# if __name__ == "__main__":

#     animals = Stack(['dog', 'cat', 'pig'])


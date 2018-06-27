#stack - first in last out, FILO

class Stack(object):

    def __init__(self, inlist):
        if inlist:
            self.stack = inlist
        else:
            self.stack = []

    def push(self, item):

        self.stack.append(item)

    def pop(self):

        if self.is_empty():
            return None

        else:
            self.stack.pop()

    def is_empty(self):
        if self.stack == []:
            return True

        return False

    def empty(self):

        self.stack = []

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]


    def length(self):

        return len(self.stack)



# code only executes when I run the module as a pgram 
if __name__ == "__main__":
    animals = Stack(['dog', 'cat', 'horse'])

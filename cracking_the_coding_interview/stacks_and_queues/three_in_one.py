###question 3.1###

#Describe how you could use a single array to implement three stacks

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


class Solution(object):
    def arrayToStack(self, inlist):

        leng = len(inlist)

        #number of elements within each queue
        num_elem = leng/3
       

        stack = Stack()
        for _ in range(3):

            if extra_elem > 0:
                extra_elem -= 1
                #number of elements which will have one extra element
                num_elem  = leng % 3 + 1 

            for num in num_elem:
                stack.push(num)

            num_elem = leng % 3

        return stack











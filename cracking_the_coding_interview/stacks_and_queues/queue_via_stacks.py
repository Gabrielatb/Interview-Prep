###3.4####
#Implement a MyQueue Class which implements a queue using two stacks


#approach: going to get both queues creates nodes from them and

#s1 = []
#s2 = [10]

#queue = [9,10]
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.s2 == []:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        return self.s2.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s2 == []:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
            
            
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.s1 == [] and self.s2 == []:
            return True
        return False





if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.push(6)
    obj.push(7)
    obj.push(8)

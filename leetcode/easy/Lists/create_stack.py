# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMax() -- Retrieve the max element in the stack.
# Example:

# MaxStack maxStack = new MaxStack();
# maxStack.push(-2);
# maxStack.push(0);
# maxStack.push(-3);
# maxStack.getMin();   --> Returns -3.
# maxStack.pop();
# maxStack.top();      --> Returns 0.
# maxStack.getMin();   --> Returns -2.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))
        
    def pop(self):
        """
        :rtype: void
        """
    
        self.min.pop()
        return  self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.stack.append(x)
        if not self.max:
            self.max.append(x)
        else:
            self.max.append(max(x, self.min[-1]))
        
    def pop(self):
        """
        :rtype: void
        """
    
        self.max.pop()
        return self.stack.pop()     

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]

        
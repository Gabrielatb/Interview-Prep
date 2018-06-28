###3.3###

#capacity = 3, so once stack cannot exceed 10 plates



#stacks = [[1,2,3],[4,5,6] [7,8,9]]
class SetOfStacks(object):

    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity 

    def push(self, item):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([item])

        else:
            self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks) == 0:
            return None

        elif len(self.stacks):
            self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks[-1].pop()

    def pop_at(self, index):
        if len(self.stacks) <= index:
            return None
        else:
            self.stacks.pop(index)





if __name__ == "__main__":
    stack = SetOfStacks(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.stacks

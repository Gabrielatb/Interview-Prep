###3.3###

#capacity = 3, so once stack cannot exceed 10 plates



#stacks = [[1,2,3,4,5][]


class SetOfStacks(object):

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity 


    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append([data])

        elif len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(data)

        elif len(self.stack[-1]) == self.capacity:
            self.stack.append([data])

        return self.stack

    def pop(self):
        if len(self.stack) == 0:
            return "cannot pop"

        elif len(self.stack[-1]) == 1:
            self.stack.pop()

        else:
            self.stack[-1].pop()

        return self.stack

    def pop_at(self, num):
        if len(self.stack) <= num:
            print "index out of range"

        else:
            self.stack[num].pop(num)

        return self.stack





if __name__ == "__main__":
    stack = SetOfStacks(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.stacks



if __name__ == "__main__":
    plates = SetOfStacks(3)
    plates.push(1)
    plates.push(2)
    plates.push(3)
    plates.push(4)
    plates.push(5)
    plates.push(6)
    plates.push(7)
    plates.push(8)









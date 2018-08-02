class SortedSack(object):

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, item):
        if len(self.stack) > 0:
            for index, elem in enumerate(self.stack[::-1]):
                if item < elem:
                    self.stack.append(item)
                    break

                else:
                    self.temp.append(self.stack.pop())
                    if len(self.stack) == 0:
                        self.stack.append(item)
                        break

            while len(self.temp) > 0:
                self.stack.append(self.temp.pop())
        else:
            self.stack.append(item)

        return self.stack



    def pop(self):
        self.stack.pop()
        return self.stack

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        return True



if __name__ == "__main__":
    stck = SortedSack()
    stck.push(1)
    stck.push(2)
    stck.push(3)
    stck.push(4)
    stck.push(5)



#4.9


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sequence(root):
    # queue = [root]
    # seq = []

    # while queue:
    #     root = queue.pop(0)
    #     if root.left is None and root.right is None:
    #         break
    #     level = [root.data]

    #     if root.left:
    #         level.append(root.left.data)
    #         queue.append(root.left)
    #     if root.right:
    #         level.append(root.right.data)
    #         queue.append(root.right)
    #     seq.append(level)
    #     level = [root.data]
    #     if root.right:
    #         level.append(root.right.data)
    #     if root.left:
    #         level.append(root.left.data)
    #     seq.append(level)

    # return seq




if __name__ == '__main__':
 
    # one = BT(1)
    # three = BT(3)
    # two = BT(2, one, three)

    ten = BT(10)
    six = BT(6)
    seven = BT(7, six, ten)
    one = BT(1)
    four = BT(4, one)
    five = BT(5, four, seven)


  #      5
  #    /   \
  #   4     7
  #  /     / \
  # 1     6   10











                                                                                                                              
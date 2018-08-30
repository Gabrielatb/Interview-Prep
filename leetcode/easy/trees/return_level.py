#return level of node in given Tree

#     3
# 2        4
#   1


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


if __name__ == "__main__":
    one = BT(1)
    two = BT(2, None, one)
    four = BT(4)
    three = BT(3, two, four)

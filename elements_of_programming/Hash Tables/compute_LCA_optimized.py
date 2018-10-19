# Design an alg, for computing LCA of two nodes in a binary tree, alg time complexity
#should ony depend on the distance from the nodes to the LCA
# p=2, q=7, result = 1
# p=2, q=5, result = 2
#         (1)
#     2          3

# 4     5     6     7


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def find_LCA(root):
    pass


if __name__ == '__main__':
    import doctest

    four = BT(4)
    five = BT(5)
    two = BT(2, four, five)
    six = BT(6)
    seven = BT(7)
    three = BT(3, six, seven)
    one = BT(1, two, three)

    if doctest.testmod().failed == 0:
        print '******* ALL TESTS PASSED! *******'
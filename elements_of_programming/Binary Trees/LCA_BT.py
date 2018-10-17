#Design Algorithm to compute the LCA of two nodes in which nodes


# p=2, q=7, result = 1
# p=2, q=5, result = 2
#         (1)
#     2          3

# 4     5     6     7

################################################################################
# Time Complexity O(n)
# Space Complexity O(h)
class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def find_LCA_helper(root, p, q, keys):

    if root is None:
        return None

    if root.val == p:
        keys[0] = True
        return root
    if root.val == q:
        keys[1] = True
        return root

    left = find_LCA_helper(root.left, p, q, keys)
    right = find_LCA_helper(root.right, p, q, keys)

    if left and right:
        return root.val

    if left:
        return left.val
    if right:
        return right.val
##################################################################################
#taking into account if one key or both keys are not present

def find(root, data):
    if root is None:
        return False

    if root.val == data:
        return True

    return find(root.left, data) or find(root.right, data)



def find_LCA(root, p, q):
    """
    >>> find_LCA(one, 2, 7)
    1

    >>> find_LCA(one, 2, 5)
    2

    >>> find_LCA(one, 2, 100)

    """

    keys = [False, False]

    lca = find_LCA_helper(root, p, q, keys)
    # print keys
    if keys[0] == True and keys[1] == True or keys[0] == True and find(root, q) or keys[1] == True and find(root, p):
        return lca

    return None


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

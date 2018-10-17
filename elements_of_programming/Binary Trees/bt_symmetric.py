#Validate if a tree is symmetric


##############################################################################
# Time COmplexity O(n)
# Space Complexity O(h)
class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def helper(l, r):
    """
    >>> is_symmetric(one)
    True

    >>> is_symmetric(one2)
    False

    >>> is_symmetric(None)
    True


    """
    if l is None and r is None:
        return True

    elif l is None and r:
        return False

    elif r is None and l:
        return False

    elif l.val != r.val:
        return False

    return helper(l.left, r.right) and helper(l.right, r.left)

def is_symmetric(root):
    if root is None:
        return True

    return helper(root.left, root.right)

################################################################################
if __name__ == '__main__':
    import doctest
    three = BT(3)
    four = BT(4)
    three2 = BT(3)
    four2 = BT(4)
    two = BT(2, three, four)
    two2 = BT(2, four2, three2)
    one = BT(1, two, two2)

    three3 = BT(3)
    three4 = BT(3)
    two3 = BT(2, None, three3)
    two4 = BT(2, None, three4)
    one2 = BT(1, two3, two4)
    
    if doctest.testmod().failed == 0:
        print '******ALL TESTS PASSED*****'

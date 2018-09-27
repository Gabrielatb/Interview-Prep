
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right



#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

#Space: O(h)
#Time: O(n)
def is_symmetric(root):


    def helper(l, r):

        if l is None and r is None:
            return True

        if l is None or r is None:
            return False

        if l.val != r.val:
            return False

        return helper(l.left, r.right) and helper(l.right, r.left)


    return helper(root.left, root.right)

if __name__ == '__main__':

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
    print is_symmetric(one)
    print is_symmetric(one2)

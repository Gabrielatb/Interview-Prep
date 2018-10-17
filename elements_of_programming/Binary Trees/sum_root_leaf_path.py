#################################################################################

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

#Time Complexity O(n)
#Space Complexity O(h)

# class BT(object):
#     def __init__(self, data, left=None, right=None):
#         self.val = data
#         self.left = left
#         self.right = right



# def sum_paths(root):
#     if root is None:
#         return ['']

#     if root.left is None and root.right is None:
#         return [str(root.val)]


#     return map(lambda x:str(root.val) + x, sum_paths(root.left)) + map(lambda x: str(root.val) + x, sum_paths(root.right))
    

# def sum_(root):
#     lst = sum_paths(root)

#     count = 0
#     for num in lst:
#         count += int(num)
#     return count

# if __name__ == '__main__':
#     five = BT(5)
#     one = BT(1)
#     zero = BT(0)
#     nine = BT(9, five, one)
#     four = BT(4, nine, zero)

#     print sum_(four)


################################################################################
#Consider a binary tree in which in which each node contains a binary digit 

#Design an algorithm to compute the sum of the binary numbers represented by the
#root-to-leafs path

#return list of sum of all possible paths
class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def sum_root_to_leaf(root, count=0):

    if root is None:
        return 0
    

    count = count * 10 + root.val
    print count

    if root.left is None and root.right is None:
        return count

    return sum_root_to_leaf(root.left, count) + sum_root_to_leaf(root.right, count)


if __name__ == '__main__':
    five = BT(5)
    one = BT(1)
    zero = BT(0)
    nine = BT(9, five, one)
    four = BT(4, nine, zero)

    print sum_root_to_leaf(four)

 

    # P = BT(0)
    # O = BT(0, None, P)
    # N = BT(0)
    # M = BT(1)
    # L = BT(1, None, M)
    # K = BT(0, L, N)
    # J = BT(0, None, K)
    # I = BT(1, J, O)
    # H = BT(0)
    # G = BT(1, H) 
    # F = BT(1, None, G)
    # E = BT(1)
    # D = BT(0)
    # C = BT(0, D, E)
    # B = BT(0, C, F)
    # A = BT(1, B, I)

  
















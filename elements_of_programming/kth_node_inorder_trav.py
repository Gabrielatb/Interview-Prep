# Given the binary tree and you have to find out the n-th node of inorder traversal.

# Examples:

# Input : n = 4
#               1
#             /   \
#            2     3
#          /   \
#         4     5
# Output : 1
# Inorder Traversal is : 4 2 5 1 3

# Input :  n = 3
#             7
#           /   \
#          2     3
#              /   \
#             8     5
# Output : 8
# Inorder: 2 7 8 3 5
# 3th node is 8


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def find_nth(root, n):

  if root is None:
    return 

  left = find_nth(root.left, n-1)

  if left  == 0:
    return root

  return find_nth(root.right, n-1)




if __name__ == '__main__':
    four = BT(4)
    five = BT(5)
    two = BT(2, four, five)
    three = BT(3)
    one = BT(1, two, three)
    print find_nth(one, 4)
    

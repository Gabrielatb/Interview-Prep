# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
#two given nodes in the BST.

# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
#              according to the LCA definition.
# Note:

# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

   if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    else:
        return left or right



   #      _______3______
   #     /              \
   #  ___5__          ___1__
   # /      \        /      \
   # 6      _2       0       8
   #       /  \
   #       7   4

if __name__ == '__main__':
    seven = TreeNode(7)
    four = TreeNode(4)
    two = TreeNode(2, seven, four)
    six = TreeNode(6)
    five = TreeNode(5, six, two)
    zero = TreeNode(0)
    eight = TreeNode(8)
    one = TreeNode(1, zero, eight)
    three = TreeNode(3, five, one)
    print lowestCommonAncestor(three, 5, 1)




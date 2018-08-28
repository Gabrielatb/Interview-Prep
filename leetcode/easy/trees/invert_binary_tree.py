# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

























# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         #non-recursive solution
#         if root is not None:
#             queue = [root]
#             while queue:
#                 node = queue.pop(0)
#                 curr_left = node.left
#                 curr_right = node.right
#                 node.left = curr_right
#                 node.right = curr_left
#                 if node.left is not None:
#                     queue.append(node.left)
#                 if node.right is not None:
#                     queue.append(node.right)

#         return root

#         #recursive solution
#         if root is None:
#             return 
#         right = self.invertTree(root.right)
#         left = self.invertTree(root.left)
#         root.left = right
#         root.right = left

#         return root
                


# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True
# Example 2:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# Output: False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is not None:
            queue = [root]
            list_val = [root.val]
            while queue:
                node = queue.pop(0)
                list_val.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                for i in list_val:
                    if (k-i) in list_val and k!=2*i:
                        return True
        return False
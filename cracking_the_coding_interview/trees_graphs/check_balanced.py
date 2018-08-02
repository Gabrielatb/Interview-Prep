#implement a function to check if a bt is balanced

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.balanced = True
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.height(root)
        return self.balanced
        
    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        if abs(left - right) > 1:
            self.balanced = False
        
        return max(left, right) + 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Time: O(n)
# Space: O(h)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root):
            if root is None:
                return 0
            
            
            left = helper(root.left)
            right = helper(root.right)
            
            if left == -1 or right == -1 or abs(right -left ) > 1:
                return -1
            
            return max(left, right) + 1
            
            
            
        if helper(root) == -1:
            return False
        return True
        
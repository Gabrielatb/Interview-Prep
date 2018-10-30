# Given two binary trees merge them into a new binary tree.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # if t1 is None and t2 is None:
        #     return 
        
        # if t1 is None and t2:
        #     return t2
        
        # if t2 is None and t1:
        #     return t1
        
        # if t1 and t2:
        #     t1.val += t2.val
            
        # if t2.left:
        #     t1.left = self.mergeTrees(t1.left, t2.left)
            
        # if t2.right:
        #     t1.right = self.mergeTrees(t1.right, t2.right)
            
        # return t1


###############################################################################
#cleaner solutino
        if t2 is None:
            return t1
        
        if t1 is None:
            return t2
        
        t1.val += t2.val
            
        t1.left = self.mergeTrees(t1.left, t2.left)
            
        t1.right = self.mergeTrees(t1.right, t2.right)
            
        return t1



#4.10

#leetcode problem as well
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None:
            return True


        res = self.check_subtree(s, t)
        
        print "under res" 
        if s.left:
            res = res or self.isSubtree(s.left,t)

        if s.right:
            res = res or self.isSubtree(s.right, t)

        return res  
            
    def check_subtree(self, s, t):
        
        if s is None and t is None:
            return True
        
        

        if (s is None and t) or (s and t is None):
            return False
        
        if s.val != t.val:
            return False

        return self.check_subtree(s.left, t.left) and self.check_subtree(s.right, t.right)
    
        
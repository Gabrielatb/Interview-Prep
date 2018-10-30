# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None:
            return False
        
        if q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
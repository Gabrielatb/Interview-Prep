# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ans = 0
        queue = [root]
        if root is None:
            return 0
        while queue:
            node = queue.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    ans += node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return ans
        
        

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest
# path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# ##############################################################################
# Time: O(n)
# Space: O(h)        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left = self.maxDepth(root.left) 
        right = self.maxDepth(root.right) 
        
        return max(left, right) + 1


################################################################################
# Time: O(n)
#Space: O(n)       
#         if root is None:
#             return 0
        
#         queue = [root]
#         count = 0
      
        
#         while queue:
#             new_level = []
#             count +=1
#             for node in queue:
#                 if node.right:
#                     new_level.append(node.right)
#                 if node.left:
#                     new_level.append(node.left)
                    
#             queue = new_level
#         return count
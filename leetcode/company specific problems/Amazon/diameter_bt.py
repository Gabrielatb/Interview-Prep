# Given a binary tree, you need to compute the
# length of the diameter of the tree. The diameter
# of a binary tree is the length of the longest path
# between any two nodes in a tree. This path may or may
# not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented
# by the number of edges between them.

# Time: O(n)
# Space: O(h)
class Solution(object):
    def __init__(self):
        self.max = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
        
            #Post oder traversal 
            #for very node add left and right depth 
            #save max
            
            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            self.max = max(self.max, left+right)
            
            return max(left, right) + 1
    
    
        if root is None:
            return 0
        
        helper(root)
        return self.max



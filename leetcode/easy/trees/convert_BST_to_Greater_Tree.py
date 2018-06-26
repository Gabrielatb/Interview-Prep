# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    
        #reverse in order traversal  
        #I visit each node once and must keep track of the nodes I previously visited which are greater
        #than the node I'm on and add them to make the new total of the node I am on
        
        stack = []
        node = root
        total = 0
        
        while len(stack) != 0 or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
                
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
            
        return root
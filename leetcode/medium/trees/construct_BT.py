# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
   
        
        
        
        
        return root
        
        
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7





class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        inorder_index = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])
        
        return root




        
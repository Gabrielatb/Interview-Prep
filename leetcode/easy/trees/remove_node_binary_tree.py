# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMin(self, root):
        while root.left is not None:
            root = root.left
        return root
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root is None:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None and root.right is not None:
                root = root.right
            elif root.right is None and root.left is not None:
                root = root.left
            elif root.left is not None and root.right is not None:
                min_value = self.findMin(root.right)
                root.val = min_value.val
                root.right = self.deleteNode(root.right, min_value.val)
                

        return root
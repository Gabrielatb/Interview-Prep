# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:

#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #iterative
    #time complexity = Space complexity : \mathcal{O}(H)O(H) to keep the recursion stack, i.e. \mathcal{O}(\log N)O(logN) in the average case, and \mathcal{O}(N)O(N) in the worst case.
    #O(1) since it's a constant space solution.
    def insertIntoBST(self, root: TreeNode, val: int):
        curr = root
        parent = None

        while curr:
            parent = curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
                
        if parent is None:
            return TreeNode(val)
        elif parent.val < val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root

    # recursive
    #Space/time complexity: \mathcal{O}(H)O(H) to keep the recursion stack, i.e. \mathcal{O}(\log N)O(logN) in the average case, and \mathcal{O}(N)O(N) in the worst case.
    def insertIntoBST(self, root: TreeNode, val: int): 
        if root is None:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
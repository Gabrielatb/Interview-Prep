# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrderTraversal(self, root, nums):
        if root is None:
            return None
        if root.left:
            left = root.left
            self.inOrderTraversal(left, nums)
        nums.append(root.val)
        if root.right:
            right = root.right
            self.inOrderTraversal(right, nums)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #edge cases if root is none return none
        
        
        #recursive solution
        
        nums = []
        
        self.inOrderTraversal(root, nums)
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
        
        
        





if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    # five_three = BinarySearchNode(5)
    # one_two = BinarySearchNode(3)
    # one = BinarySearchNode(1)
    # five_two = BinarySearchNode(5, None, five_three)
    # four = BinarySearchNode(2, one, one_two)
    # five = BinarySearchNode(5, four, five_two)

    three = BinarySearchNode(3)
    one = BinarySearchNode(1)
    two = BinarySearchNode(2, one, three)
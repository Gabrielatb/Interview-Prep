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

# Runtime O(n)
# Space O(h)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):
            
            if root is None:
                return True
            res = helper(root.left)
            
            if self.prev is None:
                self.prev = root.val
            else:
                if root.val <= self.prev:
                    res = False
                self.prev = root.val
                    
            res = res and helper(root.right)
            
            return res
        
        self.prev = None
        return helper(root)
        return res




class BT(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Runtime O(N)
# Space O(N)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):


            if root.left:
                left = helper(root.left)
                
            self.nums.append(root.val)

            if root.right:
                right = helper(root.right)
        

        if root is None:
            return True
        
        self.nums = []
        helper(root)
        print self.nums
        for i in range(len(self.nums)-1):
            if self.nums[i] >= self.nums[i+1]:
                return False
        return True
            




if __name__ == '__main__':
    zero = BT(0)
    two = BT(2)
    four = BT(4)
    six = BT(6)
    one = BT(1, zero, two)
    five = BT(5, four, six)
    three = BT(3, one, five)
    print three.isValidBST(three)




























# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            result = []
            if root is None:
                return []
            if root.left is None and root.right is None:
                result.append(str(root.val))
            
            elif root.left is None:
                for num in helper(root.right):
                    result.append(str(root.val) + str(num))
        
            elif root.right is None:
                for num in helper(root.left):
                    result.append(str(root.val) + str(num))
                                  
            else:
                for num in helper(root.right) + helper(root.left):
                    result.append(str(root.val) + str(num))
                                  
            return result
            
            
        if root is None:
            return 0
        
        result = []
        for num in helper(root.right) + helper(root.left):
             result.append(str(root.val) + num)
        
        if result == []:
            return root.val
        
        total = 0
        for num in result:
             total += int(num)                              
                                           
                                           
                                           
        return total
        
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def sumHelper(root, total, sum_n):
            
            if not root.left and not root.right:
                return total + (sum_n * 10 + root.val)

            if root.left:
                total = sumHelper(root.left, total, sum_n*10+root.val)

            if root.right:
                total = sumHelper(root.right, total, sum_n*10+root.val)

            return total
        
        if not root:
            return 0
        
        return sumHelper(root, 0, 0)



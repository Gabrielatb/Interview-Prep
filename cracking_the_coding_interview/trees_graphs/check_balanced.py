#4.4


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


#Time Complexity O(n)

#Space complexity O(1)
def balanced(root):

    if root is None:
        return 0


    left = self.balanced(root.left)

    right = self.balanced(root.right)


    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1

    return max(left,right) + 1


def check_balanced(root):
    if balanced(root) == -1:
        return False
    return True




#                 3
            # 9      20
            #     15     7






















#implement a function to check if a bt is balanced

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def __init__(self):
#         self.balanced = True
        
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
        
#         self.height(root)
#         return self.balanced
        
#     def height(self, root):
#         if root is None:
#             return 0
        
#         left = self.height(root.left)
#         right = self.height(root.right)
        
#         if abs(left - right) > 1:
#             self.balanced = False
        
#         return max(left, right) + 1
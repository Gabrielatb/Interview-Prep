# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorderSuccessor(self, root, p):
    
    if root is None:
        return None
    
    if p.val < root.val:
        return self.inorderSuccessor(root.left, p) or root
    
    return self.inorderSuccessor(root.right,p)


# class Solution(object):
#     def inorderSuccessor(self, root, p):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :rtype: TreeNode
#         """
        
#         if root is None:
#             return None
        
#         lst = []

#         while root:
#             if root.val > p.val:
#                 lst.append(root.val)
#                 root = root.left
                
#             elif root.val < p.val:
#                 root = root.right
#             else:
#                 if root.right is None:
#                     if lst == []:
#                         return 
#                     else:
#                         print lst
#                         return lst[-1]
#                 else:
#                     root = root.right
#                     while root.left:
#                         root = root.left
                    # return root
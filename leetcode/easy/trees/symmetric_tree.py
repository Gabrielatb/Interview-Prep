# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

class BT(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.val = key

        self.left = left
        self.right = right

    # Runtime: O(n)
    #Space Complexity: O(n)


    def is_symmetric(self, root):


        if root is None:
            return True
        
        queue = [root]
        
        
        while queue:
            new_level = []
            length = len(queue) /2
            for i in range(length):
                node1 = queue[i]
                node2 = queue[-(i+1)]
                if node1 == '' or node2 == '':
                    if node1 != node2:
                        return False
                    
                else:
                    if node1.val != node2.val:
                        return False

            for node in queue:
                if node != '':
                    if node.left:
                        new_level.append(node.left)
                    else:
                        new_level.append('')

                    if node.right:
                        new_level.append(node.right)
                    else:
                        new_level.append('')
                    
            queue = new_level
            
        return True
            


if __name__ == '__main__':
    three = BT(3)
    three2 = BT(3)
    two = BT(2, None, three)
    two2 = BT(2, None, three2)
    one = BT(1, two, two2)

    print one.is_symmetric(one)





















#Runtime O(n)
#Space Complexty O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def helper(self, root1, root2):
#         if root1 is None and root2 is None:
#             return True
#         elif root1 is None or root2 is None:
#             return False
#         #by this point we reassured that both roots are present
#         elif root1.val != root2.val:
#             return False
#         return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
        
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
#         return self.helper(root.left, root.right)
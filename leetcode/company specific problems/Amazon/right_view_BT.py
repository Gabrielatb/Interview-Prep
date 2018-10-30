# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


#Time: O(n)
#Space: O(n)

#Breadth First Search Solution
# class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root is None:
#             return []
#         curr = root
#         return_lst = []
#         queue = [root]

#         while queue:
#             new_level = []
#             right_node = queue[0]
#             return_lst.append(right_node.val)
#             for node in queue:
#                 if node.right:
#                     new_level.append(node.right)
#                 if node.left:
#                     new_level.append(node.left)
                    
#             queue = new_level 
#         return return_lst


#Depth First Search Solution

# Time: O(n)
# Space: O(n) ---> The height of the tree can be equivalent to n

class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def rightSideView(root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view


if __name__ == '__main__':
    four = BT(4)
    two = BT(2, four)
    three = BT(3)
    one = BT(1,two, three)
    print rightSideView(one)
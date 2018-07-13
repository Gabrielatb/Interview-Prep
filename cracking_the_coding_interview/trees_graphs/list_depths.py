# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

#first attempt 
#time complexity? -- O(n**2)
#space complexity O(n)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        level = [root]
        res = []
        next_level = []
        
        while len(level) > 0:
            res_add = []
            for node in level[::-1]:
                res_add.append(node.val)
            res.append(res_add)
            res_add = []
            for node in level:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
                    
            level = next_level
            next_level = []
            
        return res
    

#Given binary tree, design algorithm creates linked list, of all nodes in each at each depth 

class LinkedList(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):
    def levelOrderLinkedList(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return None

        level = [root]
        next_level = []

        while len(level) > 0:
            prev = None
            for node in level[::-1]:
                node.next = prev
                prev = node
            for node in level:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
                    
            level = next_level
            next_level = []








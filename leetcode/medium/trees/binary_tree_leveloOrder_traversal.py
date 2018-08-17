# Given a binary tree, return the level order traversal of its nodes' values.
#(ie, from left to right, level by level).

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

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def level_order(self, root):
        if root is None:
            return []
        
        q, result = [root], []
        
        while len(q):
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
            
        return result
                    





if __name__ == "__main__":
    nine = TreeNode(9)
    fifteen = TreeNode(15)
    seven = TreeNode(7)
    twenty = TreeNode(20, fifteen, seven)
    three = TreeNode(3, nine, twenty)


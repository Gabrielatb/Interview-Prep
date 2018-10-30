# Implement an iterator over a binary search tree (BST). 
# Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) 
# time and uses O(h) memory, where h is the height of the tree.


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left

        
# return a boolean, whether we have a next smallest number
    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) > 0:
            return True
        return False
        
# @return an integer, the next smallest number
    def next(self):
        """
        :rtype: int
        """
        node =  self.stack.pop()
        node_right = node.right
        while node_right:
            self.stack.append(node_right)
            node_right = node_right.left
        return node.val
        
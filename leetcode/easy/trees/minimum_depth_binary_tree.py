# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.data = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def min_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    #Time complexity O(n), worst case scenario traverse entire tree




        #iterative solution
 ################################################################################ 



        # count = 0
        # if root is not None:
        #     queue = [root]
        #     while queue:
        #         count +=1 
        #         for _ in range(len(queue)):
        #             node = queue.pop(0)
        #             if node.left is None and node.right is None:
        #                 return count
        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)
        
        # return count
              
            #alternative iterative solution
        # if self is None:
        #     return -1

       
        # level_number = 0
        # # levels_visited = []
        # level_char = [self]

        # while level_char:
        #     level_number += 1
        #     next_level = []
        #     for node in level_char:
        #         if node.left is None and node.right is None:
        #                 return level_number
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     level_char = next_level

        #recursive solution
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1



        #alternate recursive solution
        if root is None:
            return 0
        
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)
        
        if root.left is None or root.right is None:
            return max(left, right) + 1
        
        return min(left, right) + 1





        

if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    seventeen = BinarySearchNode('seventeen')
    fifteen = BinarySearchNode('fifteen')
    twenty = BinarySearchNode('twenty', fifteen, seventeen)
    nine = BinarySearchNode('nine')
    three = BinarySearchNode('three', nine, twenty)
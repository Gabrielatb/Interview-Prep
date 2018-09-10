# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5 


# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

#example:
# longest path between left and right subtree
#

#O(N) time: Visiting each node
#O(N) space: call stack

class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def find_diameter(self, root):

        ans = self.ans

    

        def find_longest_path(self, root):

            if root is None:
                return 0
            left = find_longest_path(self.left)
            right = find_longest_path(self.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right) + 1


        find_longest_path(root)
        return self.ans


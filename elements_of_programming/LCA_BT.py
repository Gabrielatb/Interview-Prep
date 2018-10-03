# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.


#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.
# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
#              according to the LCA definition.
# Note:

# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right



def lca(root, p, q):

    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    l = lca(root.left, p, q)
    r = lca(root.right, p, q)

    if l and r:
        return root
 
    return l or r






    
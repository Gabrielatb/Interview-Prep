



# Time: O(n)
# Space: O(h)

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
        
#         if root is None:
#             return None

#         if root.val == p.val or root.val == q.val:
#             return root
   
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
        
#         if left and right:
#             return root
        
#         if left:
#             return left
        
#         if right:
#             return right
#         

#edge case if p or q are not present

class Solution(object):
    def find_node(self, root, node):
        if root is None:
            return None
        
        if root.val == node.val or self.find_node(root.right, node) or self.find_node(root.left, node):
            return True
        
        return False
    
    def find_lca(self, root, p, q,v):
        
        if root is None:
            return None

        if root.val == p.val:
            v[0] = True
            return root
        if root.val == q.val:
            v[1] = True
            return root
   
        left = self.find_lca(root.left, p, q, v)
        right = self.find_lca(root.right, p, q, v)
        
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        v = [False, False]
        
        lca = self.find_lca(root, p, q, v)
        
        if v[0] and v[1] or v[0] and self.find_node(lca, q) or v[1] and self.find_node(lca, p):
            return lca
        
        return None
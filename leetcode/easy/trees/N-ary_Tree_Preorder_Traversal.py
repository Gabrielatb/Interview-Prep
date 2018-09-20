"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # space O(n)
        # runtime O(n)
        self.lst = []
        def helper(root):
        
            if root is None:
                return 
            
            self.lst.append(root.val)
            for child in root.children:
                helper(child)
            
         

        helper(root)
        return self.lst
        
        #Runtime: O(n)
        #Space complexity: O(n)
        
#         if root is None:
#             return []
        
#         return_lst = []
        
#         stack = [root]
        
#         while stack:
#             node = stack.pop()

#             return_lst.append(node.val)
#             for child in node.children[::-1]:
#                 stack.append(child)
#         return return_lst
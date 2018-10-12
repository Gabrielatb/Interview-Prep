# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
#key of the original BST is changed to the original key plus sum of all keys greater
# than the original key in BST.

# Example:

# Input: The curr of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The curr of a Greater Tree like this:
#              18
#             /   \
#           20     13


#Recursive
#Time Complexity O(n)
#Space Complexity O(h)

class BST(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
        self.count = 0

    def convertBST_helper(self, root):


        if root is not None:
            self.convertBST_helper(root.right)
            self.count += root.val
            self.convertBST_helper(root.left)

        return root
      

#Time Complexity O(n)
#Space Complexity O(n)


# class BST(object):
#     def __init__(self, data, left=None, right=None):
#         self.val = data
#         self.left = left
#         self.right = right



        def greater_tree(self, root):
            stack = []
            total = 0
            curr = root
            
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.right
                    
                curr = stack.pop()
                total += curr.val
                curr.val = total
                curr = curr.left
                
            return root
       

# if __name__ == '__main__':
#     two = BST(2)
#     thirteen = BST(13)
#     five = BST(5, two, thirteen)

#     import doctest
#     if doctest.testmod().failed == 0:
#         print '***Solution Passed***'









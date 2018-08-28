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



#Time Complexity O(n)
#Space Complexity O(h)

class BST(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


        #reverse inorder traversal 

    def greater_tree(self, root):
        """
        >>> five.greater_tree(five)
        18
        """

        stack = []
        curr = root
        total = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            total += curr.val
            curr.val = total
            curr = curr.left

        return root.val


if __name__ == '__main__':
    two = BST(2)
    thirteen = BST(13)
    five = BST(5, two, thirteen)

    import doctest
    if doctest.testmod().failed == 0:
        print '***Solution Passed***'









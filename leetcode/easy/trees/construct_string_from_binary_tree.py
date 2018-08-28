# You need to construct a string consists of parenthesis and integers from a 
#binary tree with the preorder traversing way.

# The null node needs to be represented by empty parenthesis pair "()". 
#And you need to omit all the empty parenthesis pairs that don't affect the 
#one-to-one mapping relationship between the string and the original binary tree.

# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     

# Output: "1(2(4))(3)"

# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 

# Output: "1(2()(4))(3)"

# Explanation: Almost the same as the first example, 
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def construct_string(self, root):
        """
        >>> one.construct_string(one)
        '1(2(4))3)'

        >>> one_2.construct_string(one_2)
        '1(2()(4))3)'

         """
      
        if root is None:
            ''

        if root.left is None and root.right is None:
            return str(root.data)

        if root.left is not None and root.right is None:
            return str(root.data) + '(' + self.construct_string(root.left) + ')'

        if root.right is not None and root.left is None:
            return str(root.data) + '()' + '(' + self.construct_string(root.right) + ')'

        return str(root.data) + '(' + self.construct_string(root.left) + ')' + self.construct_string(root.right) + ')'
     

    def print_bt(self, root):

        if root is None:
            return None


        print root.data
        left = self.print_bt(root.left)
        right = self.print_bt(root.right)


if __name__ == '__main__':
    four = BT(4)
    three = BT(3)
    two = BT(2, four, None)
    one = BT(1, two, three)


    four_2 = BT(4)
    three_2 = BT(3)
    two_2 = BT(2, None, four_2)
    one_2 = BT(1, two_2, three_2)

    import doctest
    if doctest.testmod().failed == 0:
        print "*****Solution Success*****"




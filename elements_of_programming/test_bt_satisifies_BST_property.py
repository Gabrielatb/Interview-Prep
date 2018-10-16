#Write a program that takes as input a binary tree and checks if the tree satisfies the BST property

#      (9)
    # /     \
#   (4)      (11) -----> True
# /   \      /   \
# (2)  (5)  (10)   (12)

# f(4)
# f(12) right = None left = None
# f(11) right = 12 left = 10
# f(9) right = 12


#      (24)
    # /     \
#   (1)      (55) -----> False
       #     /   
  #      (23)  



# () ---> True

#################################################################################
#Time O(n)
#Space O(n)
# class BT(object):
#     def __init__(self, data, left=None, right=None):
#         self.val = data
#         self.left = left
#         self.right = right

# def check_lst(root, lst=[]):
#     if root is None:
#         return []


#     left = check_lst(root.left, lst) + [root.val]
#     right = check_lst(root.right)

#     return left + right

# def check_bst(root, lst=[]):
#     """

#     >>> check_bst(five)
#     False

#     >>> check_bst(nine)
#     True

#     >>> check_bst(fourteen)
#     False

#     >>> check_bst(twentyfour)
#     False

#     >>> check_bst(None)
#     True
#    """


#     lst = check_lst(root)
#     for i in range(len(lst)-1):
#         if lst[i] >= lst[i+1]:
#             return False

#     return True

#################################################################################
class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def check_bst(root, min_=float('-inf'), max_=float('inf')):
    """

    >>> check_bst(five)
    False

    >>> check_bst(nine)
    True

    >>> check_bst(fourteen)
    False

    >>> check_bst(twentyfour)
    False

    >>> check_bst(None)
    True
   """

    if root is None:
        return True

   
    return min_ < root.val < max_ and check_bst(root.left, min_, root.val) and check_bst(root.right, root.val, max_)

##################################################################################








if __name__ == '__main__':
    import doctest

    #BALANCED TREE 
    twelve = BT(12)
    ten = BT(10)
    two = BT(2)
    five = BT(5)
    four = BT(4, two, five)
    eleven = BT(11, ten, twelve)
    nine = BT(9, four, eleven)
    

    #NOT BALANCED TREE
    twentythree = BT(23)
    fiftyfive = BT(55, twentythree)
    one = BT(1)
    twentyfour = BT(24, one, fiftyfive)

    #Not BALANCED
    one = BT(1)
    fourteen = BT(1, one)
    five = BT(5, fourteen)


    if doctest.testmod().failed == 0:
        print '******ALL TESTS PASSED*****'



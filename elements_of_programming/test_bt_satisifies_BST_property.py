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


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
# >>> check_bst(nine)
#     True

#     >>> check_bst(twentyfour)
#     False
def check_lst(root, lst=[]):
    if root is None:
        return []


    left = check_lst(root.left, lst) + [root.val]
    right = check_lst(root.right)

    return left + right

def check_bst(root, lst=[]):
    """
    
    >>> check_bst(fourteen)
    False

   """



   #reverse in order

    lst = check_lst(root)
    # print lst
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False

    return True












if __name__ == '__main__':
    import doctest
    #BALANCED TREE 
    # twelve = BT(12)
    # ten = BT(10)
    # two = BT(2)
    # five = BT(5)
    # four = BT(4, two, five)
    # eleven = BT(11, ten, twelve)
    # nine = BT(9, four, eleven)
    # print check_bst(nine)

    # #NOT BALANCED TREE
    # twentythree = BT(23)
    # fiftyfive = BT(55, twentythree)
    # one = BT(1)
    # twentyfour = BT(24, one, fiftyfive)

    #Not BALANCED
    one = BT(1)
    fourteen = BT(1, one)
    # five = BT(5, fourteen)


    if doctest.testmod().failed == 0:
        print '******ALL TESTS PASSED*****'



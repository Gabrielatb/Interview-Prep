#validate if bT is BST


class BT(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(n)

# def inorder_traversal(root, lst=[]):
#     if root is None:
#         return
    

#     left = inorder_traversal(root.left, lst)
#     lst.append(root.val)
#     right = inorder_traversal(root.right, lst)
#     return lst
    
        
# def isValidBST(root):
#     """
#     :type root: TreeNode
#     :rtype: bool
#     """
#     if root is None:
#         return True

#     lst = inorder_traversal(root)
    
#     for indx in range(len(lst)-1):
#         if lst[indx] > lst[indx+1]:
#             return False
#     return True

def isValidBST(root, min_=float('-inf'), max_=float('inf')):
    """
    :type root: TreeNode
    :rtype: bool
    """

    if root is None:
        return True


    return min_ <= root.val <= max_ and isValidBST(root.left, min_, min(max_, root.val)) and isValidBST(root.right, max(min_, root.val), max_)


#   2
# / \
# 1   3






if __name__ == '__main__':
    # one = BT(1)
    # three = BT(3)
    # two = BT(2, one, three)
    # print isValidBST(two)

    # zero = BT(0)
    # print isValidBST(zero)
    three = BT(3)
    six = BT(6)
    one = BT(1)
    four = BT(4, three, six)
    five = BT(5, one, four)
    print isValidBST(five)


    
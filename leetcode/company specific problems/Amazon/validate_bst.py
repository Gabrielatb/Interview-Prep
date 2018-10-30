# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    def validate(root, left_max=float('-inf'), right_min= ('inf')):
        
        if root is None:
            return True
        
        
        return left_max < root.val < right_min and
                validate(root.left, left_max, min(root.val, right_min)) and
                validate(root.right, max(root.val, left_max), right_min)
    
    
    return validate(root)


if __name__ == '__main__':
    four = BT(4)
    two = BT(2, four)
    three = BT(3)
    one = BT(1,two, three)
    print isValidBST(one)
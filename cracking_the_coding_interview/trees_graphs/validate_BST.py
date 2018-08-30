#4.5

#Validate BST

#    2
#  /    \
# 1       3


#Time Complexity O(n)
#Space Complexity O(1)




#inorder traversal
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def validate_helper(root, left, right):
    if root is None:
        return True

    if left < root.val < right:
        return validate_helper(root.left, left, root.val) and validate_helper(root.right, root.val, right)

    return False


def validate(root):

    return self.validate_helper(root, float('-inf'), float('inf'))





if __name__ == "__main__":

    one = TreeNode(1)
    three = TreeNode(3)
    two = TreeNode(2, one, three)
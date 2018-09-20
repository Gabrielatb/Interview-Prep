# BST Has Data
# Given the root of a binary search root node and some data, determine if that
# data is in the tree.
      #       (9)
      #      /  \
      #    (6)  (12)
      #   /    /  \
      # (1)  (10)  (13)



    # >>> bst_has_data(root, 13)
    # True
    # >>> bst_has_data(root, 1)
    # False

class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#f(13) = True
#f(10), left = False, right = False
#f(12), left = False, right = True
#XXXf(1), left = False, right= False
#XXXXf(6), left= False, right = False
# f(9), left=False , right = True

def find_node(root, data):                       

 #space Complexity: O(h)
 #Time Complexity O(n)   
    #recursive                                             
    if root is None:
        return False

    if root.data == data:
        return True

    if root.data > data:
        return find_node(root.left, data)

    else:
        return find_node(root.right, data)

    #iterative 
    #space complexity = O(1)
    # Time Complexity = O(n)
    
    curr = root
    while curr:
        if curr.data == data:
            return True

        elif curr.data > data:
            curr = curr.left
        else:
            curr = curr.right

    return False

    




if __name__ == '__main__':
    one = BST(1)
    ten = BST(10)
    thirteen = BST(13)
    six = BST(6, one)
    twelve = BST(12, ten, thirteen)
    nine = BST(9, six, twelve)
    # print find_node(nine, 9)
    # print find_node(nine, 6)
    # print find_node(nine, 1)
    # print find_node(nine, 12)
    # print find_node(nine, 10)
    # print find_node(nine, 13)
    print find_node(nine, 99)
    print find_node(nine, 0)
    print find_node(nine, -1)
    print find_node(nine, 1.5)



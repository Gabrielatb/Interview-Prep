#Compute exterior of BT


#     ___1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6   
#    / \      / \
#   7   8    9  10


#[1,2,4,7,8,9,10,6,3]
class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def left_side(root, exterior):
    if root is None or root.left is None and root.right is None:
        return 

    exterior.append(root.val)
    if root.left:
        return left_side(root.left, exterior)
    elif root.right:
        return left_side(root.right, exterior)

    
def right_side(root, exterior):
    if root is None or root.left is None and root.right is None:
        return 

    exterior.append(root.val)
    if root.right:
        return right_side(root.right, exterior)
    elif root.left:
        return right_side(root.left, exterior)
   
def leaves(root, exterior):
    
        if root is None:
            return None

        if root.left is None and root.right is None:
            exterior.append(root.val)
            return

        leaves(root.left, exterior)
        leaves(root.right, exterior)

def compute_exterior(root):


    if root is None:
        return []

    exterior = [root.val]
    left_side(root.left, exterior)
   
    leaves(root.left, exterior)
    leaves(root.right, exterior)
    right_side(root.right, exterior)
    return exterior


if __name__ == '__main__':
    seven = BT(7)
    eight = BT(8)
    nine = BT(9)
    ten = BT(10)
    four = BT(4)
    five = BT(5, seven, eight)
    six = BT(6, nine, ten)
    two = BT(2, four, five)
    three = BT(3, six)
    one = BT(1, two, three)
    print compute_exterior(one)







# def find_exterior(root):

#     return_lst = [root.val]

    
#     curr = root.left
#     while curr:
#         return_lst.append(curr.val)
#         if curr.left:
#             curr = curr.left

#         elif curr.right:
#             curr = curr.right
#         else:
#             break


#     level = []
#     queue = [root]
#     curr = root
#     count = 0
    
#     while queue:
#         level = []
#         for node in queue:

#             if node.left:
#                 level.append(node.left)

#             if node.right:
#                 level.append(node.right)
#         if level == []:
          
#             for node in queue:
#                 return_lst.append(node.val)
#         queue = level
  


    
#     temp = []

#     curr = root.right
#     while curr:
#         temp.append(curr.val)
#         if curr.right:
#             curr = curr.right

#         elif curr.left:
#             curr = curr.left
#         else:
#             break
#     temp = temp[:-1]
#     return return_lst + temp[::-1]


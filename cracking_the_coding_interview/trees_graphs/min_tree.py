#given sorted array with unique integer elements, write an algorithm to create 
#binary tree


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create(lst):

#Time Complexity: O(n)
#Space Complexity O(n)

    if len(lst) == 0:
        return None

    mid = (len(lst) / 2) -1 
    node = BT(lst[mid])

    node.left = create(lst[:mid])
    node.right = create(lst[mid+1:])


    return node.data


#[1,2,3,4,5,6]


#       3
#     /   \
#     2     5
#    /    4  6
# 1

























# class Node(object):
#     def __init__(self, data):
#         self.data
#         self.left = left
#         self.right = right



# class BST(object):

#     def __init__(self, root):
#         self.root = root


#     def min_tree(self, inlist):
#         if len(inlist) == 0):
#             return None

#         mid_point = len(inlist) / 2
#         mid_element = inlist[mid_point]
#         mid_node = Node(mid_element)

   
#         mid_node.left = self.min_tree(inlist[:mid_point])
#         mid_node.right = self.min_tree(inlist[mid_point + 1:])

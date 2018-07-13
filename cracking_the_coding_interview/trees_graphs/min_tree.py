#given sorted array with unique integer elements, write an algorithm to create 
#binary tree

class Node(object):
    def __init__(self, data):
        self.data
        self.left = left
        self.right = right



class BST(object):

    def __init__(self, root):
        self.root = root


    def min_tree(self, inlist):
        if len(inlist) == 0):
            return None

        mid_point = len(inlist) / 2
        mid_element = inlist[mid_point]
        mid_node = Node(mid_element)

   
        mid_node.left = self.min_tree(inlist[:mid_point])
        mid_node.right = self.min_tree(inlist[mid_point + 1:])

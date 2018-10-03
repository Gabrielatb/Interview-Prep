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


def find_exterior(root):

    return_lst = []
            
    curr = root

    while curr:
        if curr.val not in return_lst:
                return_lst.append(curr.val)

        if curr.left:
            curr = curr.left

        elif curr.right: 
            curr = curr.right
        else:
            break





    levels = []
    queue = [root]

    while queue:
        new_level = []
        levels.append(queue)
        for node in queue:
          
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)

        queue = new_level
    levels = levels[-1]
    for node in levels:
        return_lst.append(node.val)


    curr = root
    temp  = []
    if root.right:
        curr = root
        temp  = []
        while curr:
            if curr.val not in return_lst:
                    temp.append(curr.val)

            if curr.right:
                curr = curr.right

            elif curr.left: 
                curr = curr.left

            else:
                return_lst += temp[::-1]
                break

    return return_lst



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
    print find_exterior(one)
#merge two BST to be height balanced


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
        self.lst = []


def print_bt(root):
    if root is None:
        return 

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
        temp = []
        for node1 in queue:
            temp.append(node1.val)
        print temp
    return

    # print root.val

    # print_bt(root.left)
    # print_bt(root.right)


def create_lst(root1, root2):
    if root1 is None and root2 is None:
        return []
    if root2 is None:
        return [root1]

    if root1 is None:
        return [root2]

    
    left = create_lst(root1.left, root2.left)
    right = create_lst(root1.right, root2.right)

    
    if root1.val < root2.val:
        return left + [root1, root2] + right

    return left + [root2, root1] + right


def merge(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]

    mid = len(lst) / 2
    node = lst.pop(mid)
    left = lst[:mid]
    right = lst[mid:]
    # for node_left in left:
    #     print node_left.val
    # print '**********************'
    # for node_right in right:
    #     print node_right.val
    # print '**********************'
  
    node.left = merge(left)
    node.right = merge(right)
    
   
    return node


  

def merge_BT(root1, root2):
    lst = create_lst(root1, root2)

    node = merge(lst)
    # print node.val
    # print_bt(node)
    return


if __name__ == '__main__':
    two = BT(2)
    eleven = BT(11)
    five = BT(5, two, eleven)
    twentythree = BT(23)
    seventeen  = BT(17, five, twentythree)


    three = BT(3) 
    seven = BT(7, three) 
    nineteen = BT(19)
    thirteen = BT(13, seven, nineteen)
    # print print_bt(seventeen)
    # print print_bt(thirteen)
    # print merge_BT(seventeen, thirteen)
    print merge([three, seven, nineteen, thirteen])
    # print merge_BT(seventeen, thirteen)

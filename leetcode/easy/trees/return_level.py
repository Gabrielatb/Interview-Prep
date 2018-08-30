#return level of node in given Tree

#     3
# 2        4
#   1


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_level(root,num):
    level_count = 1
    queue = [root]

    while queue: 
        node = queue.pop(0)
        level_count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if num in queue:
            return level_count

    print "Node not found"   
    return None

if __name__ == "__main__":
    one = BT(1)
    two = BT(2, None, one)
    four = BT(4)
    three = BT(3, two, four)

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.data = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def level_order(self):
        """Return node with this data.

        Start here. Return None if not found.
        """
        if self is None:
            return []

        level = [self]
        levels_visited = []
        
        while level:
            levels_visited.append([node.data for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return levels_visited


        #return queue

if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    seventeen = BinarySearchNode('seventeen')
    fifteen = BinarySearchNode('fifteen')
    twenty = BinarySearchNode('twenty', fifteen, seventeen)
    nine = BinarySearchNode('nine')
    three = BinarySearchNode('three', nine, twenty)

    # print "three = ", three.find('nine')      # should find
    # print "banana = ", money.find("banana")  # shouldn't find


    # binary_tree = N(dumbledore)
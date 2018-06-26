
class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def find(self, sought):
        """Return node with this data.

        Start here. Return None if not found.
        """

        current = self
            # print "checking ", current.data

        if current.data == sought:
            return "found " + str(current.data)

        elif sought < current.data and current.left is not None:
            current = current.left
            return current.find(sought)

        elif sought > current.data and current.right is not None:
            current = current.right
            return current.find(sought)

        else:
            return None
if __name__ == '__main__':
    # Create sample tree and search for nodes in it

    apple = BinarySearchNode("apple")
    ghost = BinarySearchNode("ghost")
    fence = BinarySearchNode("fence", apple, ghost)
    just = BinarySearchNode("just")
    jackal = BinarySearchNode("jackal", fence, just)
    zebra = BinarySearchNode("zebra")
    pencil = BinarySearchNode("pencil", None, zebra)
    mystic = BinarySearchNode("mystic")
    nerd = BinarySearchNode("nerd", mystic, pencil)
    money = BinarySearchNode("money", jackal, nerd)

    print "nerd = ", money.find("nerd")      # should find
    print "banana = ", money.find("banana")  # shouldn't find
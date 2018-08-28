            #  5
            #  /\
            # 4  6
            # /    \
            # 3     7



class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find_height(self, root):
        """
        >>> five.find_height(five)
        3
        >>> five_2.find_height(five_2)
        3


        """

        if root is None:
            return 0

        left = self.find_height(root.left)
        right = self.find_height(root.right)


        return max(left, right) + 1

# Time Complexity O(n)
# Space Complexity O(h)


if __name__ == '__main__':
    three = BT(3)
    seven = BT(7)
    six = BT(6, None, seven)
    four = BT(4, three)
    five = BT(5, four, six)

##########################
    seven_2 = BT(7)
    six_2 = BT(6, None, seven)
    four_2 = BT(4)
    five_2 = BT(5, four_2, six_2)

    import doctest
    if doctest.testmod().failed == 0:
        print '*****Tests Passed*****!'





















#find height of binary search tree

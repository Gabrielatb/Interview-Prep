# Write a program that efficiently computes the kth node appearing in an inorder traversal

# Assume each node stores the number of nodes in the subtree rooted at that node.


class BT(object):
    def __init__(self, data,left=None, right=None, size = 0):
        self.val = data
        self.left = left
        self.right = right
        self.size = size

    def find_nth(self, root, k):

        curr = root

        while curr:

            if root.left:
              left_size = root.left.size
            else:
              left_size = 0

        #k node is in right_subtree
           
            if left_size + 1 < k:
              k -= left_size + 1
              curr = curr.right

            elif left_size == k - 1:
              return curr.val

            else:
              curr = curr.left

        return None

if __name__ == '__main__':

    four = BT(4)
    five = BT(5)
    two = BT(2,four, five, 2)
    three = BT(3)
    one = BT(1,two, three, 4)
    print one.find_nth(one, 3)

# Input : n = 4
#               1
#             /   \
#            2     3
#          /   \
#         4     5
# Output : 1
# Inorder Traversal is : 4 2 5 1 3




 # def find_nth(self, root, n):

 #        if root is None:
 #            return

        
 #        self.find_nth(root.left, n)
 #        self.count += 1

 #        # print n
 #        if n == self.count:
 #            return root.val
            

 #        return self.find_nth(root.right, n)





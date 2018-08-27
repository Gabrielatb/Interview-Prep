       
# Given a non-empty binary tree, return the average value of the nodes on each queue in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on queue 0 is 3,  on queue 1 is 14.5, and on queue 2 is 11. Hence return [3, 14.5, 11].

# Time Complexity: O(n)
#Space Complexity: O(n)


class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def print_list(self,root):

        queue = [root]

        while queue:
            node = queue.pop(0)
            print node.data

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


    def average(self,root):
        level = [root]
        average = []


        while level:
            total = 0.0
            new_level = []
            for node in level:
                total += node.data
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            average.append(total/len(level))
            level = new_level

        return average







if __name__ == '__main__':
    fifteen = BST(15)
    seven = BST(7)
    nine = BST(9)
    twenty = BST(20, fifteen, seven)
    three = BST(3, nine, twenty)


################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def averageOfqueues(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[float]
#         """
#         queue = [root]
#         list_average = []
        
#         while queue:
#             total = 0.0
#             len_queue = len(queue)
#             for _ in range(len_queue):
#                 node = queue.pop(0)
#                 total += node.val
#                 if node.left is not None:
#                     queue.append(node.left)
#                 if node.right is not None:
#                     queue.append(node.right)
#             # print total
#             # print len_queue
#             list_average.append(float(total/len_queue))
#             # print list_average
            
            
#         return list_average
#             
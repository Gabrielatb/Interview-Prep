# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5



class Solution(object):
    def create_tree(self, list_nums):
        
        if not list_nums:
            return None
        mid = len(list_nums)/2
        root = TreeNode(list_nums[mid])
        root.left = self.create_tree(list_nums[:mid])
        root.right = self.create_tree(list_nums[mid+1:])
        return root
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        list_nums = []
        while head:
            list_nums.append(head.val)
            head = head.next
        root = self.create_tree(list_nums)
        return root
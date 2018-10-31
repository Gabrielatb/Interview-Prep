class Solution(object):
    def __init__(self):
        
        self.max = float('-inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root is None:
                return 0

            left_sum = helper(root.left)
            right_sum = helper(root.right)

            max_single_path = max(max(left_sum, right_sum) + root.val, root.val)

            max_total = max(max_single_path, left_sum + right_sum + root.val)

            self.max = max(self.max, max_total)

            return max_single_path
        
        
        helper(root)
        return self.max
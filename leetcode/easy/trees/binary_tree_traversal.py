class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def bfs_iterative(self,root):
        
        queue = [root]

        while queue:
            node = queue.pop(0)
            print node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs_iterative(self, root):

        stack = [root]

        while stack:
            print stack
            node = stack.pop()
            print node.data
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def dfs_preorder(self, root):

        if root is None:
            return None

        print root.data

        left = self.dfs_preorder(root.left)

        right = self.dfs_preorder(root.right)

    def dfs_postorder(self, root):

        if root is None:
            return None

        

        left = self.dfs_postorder(root.left)

        right = self.dfs_postorder(root.right)
        print root.data

    def dfs_inorder(self, root):

        if root is None:
            return None

        

        left = self.dfs_inorder(root.left)

        print root.data

        right = self.dfs_inorder(root.right)























if __name__ == '__main__':
    one = BST(1)
    three = BST(3)
    two = BST(2, one, three)
    six = BST(6)
    four = BST(4, two, six)






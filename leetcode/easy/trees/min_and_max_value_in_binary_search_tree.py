#find min/max value in binary search tree

def find_min(root):
    #iterative solution
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.data

    #recursive solution
    if root.left is None
        return root.data

    return find_min(root.left)

def find_max(root):
    #iterative solution
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root.data

    #recursive solution

    if root.right is None:
        return root.data
    return find_max(root.right)
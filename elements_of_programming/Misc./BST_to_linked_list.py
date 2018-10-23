#  Convert a BST to a sorted doubly linked list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
        self.lst = []

def convert_bt_ll(root):
    if root is None:
        return root

    if root.left:
        root.left = 

 if (root == NULL) 
        return root; 
  
    // Convert the left subtree and link to root 
    if (root->left != NULL) 
    { 
        // Convert the left subtree 
        node* left = bintree2listUtil(root->left); 
  
        // Find inorder predecessor. After this loop, left 
        // will point to the inorder predecessor 
        for (; left->right!=NULL; left=left->right); 
  
        // Make root as next of the predecessor 
        left->right = root; 
  
        // Make predecssor as previous of root 
        root->left = left; 
    } 
  
    // Convert the right subtree and link to root 
    if (root->right!=NULL) 
    { 
        // Convert the right subtree 
        node* right = bintree2listUtil(root->right); 
  
        // Find inorder successor. After this loop, right 
        // will point to the inorder successor 
        for (; right->left!=NULL; right = right->left); 
  
        // Make root as previous of successor 
        right->left = root; 
  
        // Make successor as next of root 
        root->right = right; 
    } 
  
    return root; 
# Serialization is the process of converting a data structure or object into a 
#sequence of bits so that it can be stored in a file or memory buffer, or transmitted 
#across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. 
#There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string 
#and this string can be deserialized to the original tree structure.

#    3
#  /   \
# 2     4
#  \     
#   1


#pre order traversal
#[3,2,"",1,"","",4, "", ""]



class BT(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def serialize_helper(self, root, lst=[]):
        if root is None:
            lst.append('#')
            return 

        lst.append(str(root.val))
        left = self.serialize_helper(root.left, lst)
        right = self.serialize_helper(root.right, lst)
        print "this is the list in the serialize_helper", lst
        return ''.join(lst)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        
        result = self.serialize_helper(root)
        print "this is the result ", result
        return result
    
    
    def deserialize_helper(self, lst):
        print "this is the original list ", lst
        if len(lst) == 0: 
            return None
        data = lst.pop(0)
        if data == "#":
            return None
         
        # print "this is the data I am working with ", data
        # print "this is the new list I am working with ", lst

        if data == '':
            return None

        node = BT(data)

        node.left = self.deserialize_helper(lst)
        node.right = self.deserialize_helper(lst)
  
        print node.left
        print node.right
        return node.val
                
        
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        
        lst = list(data)
        print "this is the lst ", lst
        return self.deserialize_helper(lst)


# def serialize(root, lst=[]):

#     if root is None:
#         lst.append('')
#         return 
        
#     lst.append(root.data)
#     left = serialize(root.left, lst)
#     right = serialize(root.right, lst)

# def deserialize(lst):

#     data = lst.pop(0)

#     if data == '':
#         return None

#     node = BT(data)

#     node.left = deserialize(lst)
#     node.right = deserialize(lst)

#     print 'this is right node ', node.right
#     print 'this is left node ', node.left
#     print 'this is the node ', node.data
#     return node.data





if __name__ == "__main__":
    one = BT(1)
#     two = BT(2, None, one)
#     four = BT(4)
#     three = BT(3, two, four)
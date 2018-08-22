# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

    #    1
    #   / \
    #  /   \
    # 0 --- 2
    #      / \
    #      \_/


    #curr = 2
    #dict_ = {'2': node, '0': node, '1':node}



# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    #time/space complexity: O(N)



    def generate(self, node, dict_):
        if node is None:
            return None
        copy = UndirectedGraphNode(node.label)
        dict_[copy.label] = copy

        for i in range(len(node.neighbors)):
            if node.neighbors[i].label in dict_:
                copy.neighbors.append(dict_[node.neighbors[i].label])
            else:
                copy.neighbors.append(self.generate(node.neighbors[i], dict_))

    #iteratee through neighbors of node
        #if they are in my dictionary
        #copy.neighbors.append(the node)
        #else:
            #recursively call my function(0)
    return copy


    def cloneGraph(self, node):
        return self.generate(node, dict_={})



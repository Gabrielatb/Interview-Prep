









class Graph(object):
    def __init__(self, data):

        self.label = data
        self.neighbors = []


#Depth first solution
#Time: O(n+m)
#Space: O(n)
# def deep_clone(node):

#     def helper(node, graph_clone):
#         # print type(node)

#         if node not in graph_clone:
#             graph_clone[node] = Graph(node.label)
#         else:
#             return graph_clone[node]


#         for neighbors in node.neighbors:
#             # print neighbors.label
#             graph_clone[node].neighbors.append(helper(neighbors, graph_clone))

#         return graph_clone[node]

#     graph_clone = {}
#     return helper(node, graph_clone)


#iterative solution
#breadth first search

#Time O(n+e)
#Space O(n)
def deep_clone(node):

    queue = [node]
    graph_clone = {node: Graph(node.label)}

    while queue:
        n = queue.pop(0)
    
        for neighbor in n.neighbors:
            if neighbor not in graph_clone:
                graph_clone[neighbor] = Graph(neighbor.label)
                queue.append(neighbor)

            
            graph_clone[node].neighbors.append(graph_clone[neighbor])

    return graph_clone[clone]




if __name__ == '__main__':

    zero = Graph(0)
    one = Graph(1)
    two = Graph(2)
    zero.neighbors.extend([zero,two])
    one.neighbors.extend([zero,two])
    two.neighbors.extend([two])
    print deep_clone(zero)

class Graph(object):
    def __init__(self, data):

        self.label = data
        self.neighbors = []


def deep_clone(node):

    def helper(node, graph_clone):

        if node not in graph_clone:
            graph_clone[node] = Graph(node.label)
        else:
            return graph_clone[node]


        for neighbors in node.neighbors:
             graph_clone[node].neighbors.append(helper(neighbors, graph_clone))

        return graph_clone[node]


   graph_clone = {}
   return deep_clone(node, graph_clone)





if __name__ == '__main__':

    zero = Graph(0)
    one = Graph(1)
    two = Graph(2)
    zero.neighbors.extend([1,2])
    one.neighbors.extend([0,2])
    two.neighbors.extend([2])
    print deep_clone(zero)

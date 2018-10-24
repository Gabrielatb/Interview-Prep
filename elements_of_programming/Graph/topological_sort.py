#Implementation of topological sort
#very useful for problems pertaining to task scheduler, etc


class Node(object):
    def __init__(self, data):
        self.data = data
        self.adjacent = set()



class Graph(object):
    def __init__(self):
        self.nodes = set()

    def add_nodes(self, lst):
        for node in nodes:
            self.nodes.add(node)


    def set_adjacent(self, node1, ndode2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)




if __name__ == '__main__':
    g = Graph()
    a = Node('A')
    a = Node('A')
    a = Node('A')
    a = Node('A')
    a = Node('A')
    a = Node('A')
    
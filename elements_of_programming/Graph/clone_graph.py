#Directed Graph: two fields, integer label and a list of references to other vertices

#Design an algorithm that takes reference to vertex u, and creates a copy of the Graph
#on the vertices reachable from u
#return copy u

#graph Implementation
import collections

class Node(object):

    def __init__(self, label, edges=None):
        """Create a person node with friends adjacent"""

        if edges is None:
            adjacent = set()

        self.label = label
        self.edges = adjacent



class Graph(object):
    def __init__(self):

        self.nodes = set()

    def add_nodes(self, lst):
        for node in lst:
            self.nodes.add(node)

    def set_edges(self, node1, node2):
        """Add a node to the graph """

        node1.edges.add(node2)
        node2.edges.add(node1)

    def are_connected(self, node1, node2):
        seen = set()
        queue = []
        seen.add(node1)
        queue.append(node1)

        while queue:
            node = queue.pop(0)
            if node == node2:
                return 'FOUND!'

            for child in node.edges - seen:
                queue.append(child)
                seen.add(child)
        return 'Not Connected'


    def are_edges_connected(self, node1, node2):
        if node1 in node2.edges:
            return True
        return False


    def clone(self, vertex):
        if vertex is None:
            return None


        #traverse graph breadth first search 
        queue = [vertex]
        clone = {vertex: Node(vertex.label)}

        while queue:
            vertex = queue.pop(0)
            for edge in vertex.edges:

                if edge not in clone:
                    clone[edge] = Node(edge.label)
                    queue.append(edge)

                clone[vertex].edges.add(clone[edge])
        return clone[vertex]

if __name__ == '__main__':
    graph = Graph()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    eight = Node(8)


    graph.add_nodes([one, two, three, four, five, six, seven, eight])

    
    graph.set_edges(one, two)
    graph.set_edges(two, four)
    graph.set_edges(four, five)
    graph.set_edges(three, five)
    graph.set_edges(three, two)
    graph.set_edges(two, six)
    graph.set_edges(seven, six)

    
    print graph.clone(one)


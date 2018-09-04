# given a list of projects, and list of dependencies, (list of pairs of projects

# where the second project is dependent on the first project)

#all project dependencies but be built before the project is , find a build order



#projects: a, b, c, d, e, f 
#dependencies (a,d), (f,b), (b,d), (f,a), (d,c)

#output f,e,a,b,d,c
class Node(object):
    def __init__(self, data, adjacent=set()):
        self.data = data
        self.adjacent = adjacent

class Graph(object):
    def __init__(self):

        self.nodes=set()

    def add(self, node):

        self.nodes.add(node)

    def set_nodes(self, node1, node2):

        node1.ajacent.add(node2)
        node2.adjacent.add(node1)



if __name__ == "__main__":
    graph =Graph()


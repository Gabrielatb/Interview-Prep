from queue import Queue


class Node(object):
    def __init__(self, data, adjacent=set()):

        self.data = data
        self.adjacent = adjacent


class Graph(object):
    def __init__(self):
        self.nodes=set()

    def show_adj(self, node):

        for node in node.adjacent:
            print node.data

    def add_node(self, node):
        self.nodes.add(node)


    def add_nodes(self, lst):
        for node in lst:
            self.add_node(node)

    def add_adj(self, node1, node2):

        node1.adjacent.add(node2.data)
        node2.adjacent.add(node1.data)

#     def are_connected(self, node1, node2):

#         poss_nodes =[]
#         seen = set()
#         poss_nodes.append(node1)
#         seen.add(node1)

#         while poss_nodes:
#             node = poss_nodes.pop(0)
#             print node.data
#             if node is node2:
#                 return True
#             else:
#                 for new_node in node.adjacent-seen:
#                     poss_nodes.append(new_node)
#                     seen.add(new_node)
#         return False

if __name__ == '__main__':

    harry = Node('harry')
    hermione = Node('hermione')
    ron = Node('ron')

    draco = Node('draco')
    crabbe = Node('crabbe')
    goyle= Node('goyle')

    graph = Graph()
    graph.add_nodes([harry, hermione, ron, draco, crabbe, goyle])

    # graph.add_adj(hermione, harry)
    # graph.add_adj(hermione, ron)
    # graph.add_adj(harry, ron)

    # graph.add_adj(crabbe, draco)
    # graph.add_adj(draco, goyle)
     
    # print hermione.adjacent
    # print graph.are_connected(hermione, goyle)

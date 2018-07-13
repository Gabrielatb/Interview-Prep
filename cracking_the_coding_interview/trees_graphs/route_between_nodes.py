class Node(object):

    def __init__(self, data, adjacent=None):

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set)

        self.data = data
        self.adjacent = adjacent


class Graph(object):

    def __init__(self):

        self.nodes = set()


    def add_node(self, node):

        self.nodes.add(node)


    def add_nodes(self, nodes):

        for node in nodes:
            self.nodes.add(node)

    def set_nodes(self, node1, node2):

        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def is_connected(self, node1, node2):

        to_see = Queue()
        seen= set()

        to_see.enqueue(node1)
        seen.add(node1)

        while to_see.is_empty() is False:
            node = to_see.dequeue()

            if node == node2:
                return True

            else:

                for node in node2.adjacent - seen:
                    to_see.enqueue(node)
                    seen.add(node)

    return False


    def is_connected_rec(self, node1, node2, seen=None):

        if seen is None:
            seen = set()

        if node1 == node2:
            return True

        else:
            seen.add(node1)

            for node in node1.adjacent:
                if node not in seen:
                    self.is_connected_rec(node, node2, seen)
                    return True

        return False








if __name__ == "__main__":
    harry = Node("Harry")
    hermione = Node("Hermione")
    ron = Node("Ron")
    neville = Node("Neville")
    trevor = Node("Trevor")
    fred = Node("Fred")
    draco = Node("Draco")
    crabbe = Node("Crabbe")
    goyle = Node("Goyle")

    friends = Graph()
    friends.add_nodes([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

    friends.set_nodes(harry, hermione)
    friends.set_nodes(harry, ron)
    friends.set_nodes(harry, neville)
    friends.set_nodes(hermione, ron)
    friends.set_nodes(neville, hermione)
    friends.set_nodes(neville, trevor)
    friends.set_nodes(ron, fred)
    friends.set_nodes(draco, crabbe)

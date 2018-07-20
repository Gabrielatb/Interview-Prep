"""Example of an undirected graph."""

from queue import Queue


class PersonNode(object):
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        self.name = name

        if adjacent:
            assert isinstance(adjacent, set), \
                   "adjacent must be a set!"
            self.adjacent = adjacent
        else:
            self.adjacent = set()


    def __repr__(self):
        """Debugging-friendly representation"""

        return "<PersonNode: %s>" % self.name


class FriendGraph(object):
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return "<FriendGraph: %s>" % [n.name for n in self.nodes]

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people friends? Breadth-first search."""

        to_visit = Queue()
        to_visit.enqueue(person1)
        seen = set()
        seen.add(person1)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            print "\nchecking", current
            if current is person2:
                return True
            else:
                for friend in current.adjacent - seen:
                    to_visit.enqueue(friend)
                    seen.add(friend)
                    print "added to queue:", friend
        return False


    def are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            return True

        seen.add(person1)  # Keep track that we've visited here

        for person in person1.adjacent - seen:

            if self.are_connected_recursive(person, person2, seen):
                return True

        return False


    def verbose_are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search.

        Same as FriendGraph.are_connected_recursive(), but with helpful
        print statements.
        """

        if not seen:
            seen = set()

        if person1 is person2:
            print "\nreturning True - ", person1.name, "is", person2.name
            return True

        seen.add(person1)  # Keep track that we've visited here
        print "\nchecking", person1

        for person in person1.adjacent - seen:

            print "calling method on " + person1.name + "'s friend", person.name, "with", person2.name
            if self.are_connected_recursive(person, person2, seen):
                print "\nreturning True from checking ", person1.name, "and", person2.name
                return True
        print "returning False from checking", person1.name, "and", person2.name
        return False

if __name__ == "__main__":
    # Add sample friends
    harry = PersonNode("Harry")
    hermione = PersonNode("Hermione")
    ron = PersonNode("Ron")
    neville = PersonNode("Neville")
    trevor = PersonNode("Trevor")
    fred = PersonNode("Fred")
    draco = PersonNode("Draco")
    crabbe = PersonNode("Crabbe")
    goyle = PersonNode("Goyle")

    hogwarts = FriendGraph()
    hogwarts.add_people([harry, hermione, ron,
                        neville, fred, trevor,
                        draco, crabbe, goyle])

    hogwarts.set_friends(harry, hermione)
    hogwarts.set_friends(harry, ron)
    hogwarts.set_friends(harry, neville)
    hogwarts.set_friends(hermione, ron)
    hogwarts.set_friends(neville, hermione)
    hogwarts.set_friends(neville, trevor)
    hogwarts.set_friends(ron, fred)
    hogwarts.set_friends(draco, crabbe)
    hogwarts.set_friends(draco, goyle)

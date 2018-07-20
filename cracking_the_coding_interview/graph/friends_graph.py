from queue import Queue


class PersonNode(object):
    """Creating a person """

    def __init__(self, name, adjacent=None):
        
        self.name = name

        if adjacent:
            assert isinstance(adjacent, set), \

            self.adjacent = adjacent

        else:
            self.adjacent = set()

    def __repr__(self):
        return "Person Node: {}".format(self.name)


class FriendGraph(object):
    
    def __init__(self):

        self.nodes = set()

    def add_person(self, person):

        self.nodes.append(person)

    def set_friends(self, person1, person2):

        person1.adjacent.add(person2)
        person2.adjacent.add(person2)

    def add_people(self, person_list):

        for person in person_list:
            self.add_person(person)


    def are_connected(self, person1, person2):

        to_visit = Queueu()
        to_visit.enqueue(person1)
        seen = set()
        seen.add(person1)

        while to_visit:
            current = to_visit.dequeue()
            print "checking:", current

            if current == person2:
                return True

            else:
                for friend in current.adjacent - seen:
                    #as soon as node is in to_visit it can be added in seen set
                    to_visit.enqueue(friend)
                    seen.add(friend)
                    print friend, " added to queueu"

        return False

    def are_connected_recursive(self, person1, person2, seen=None):

        if not seen:
            seen = set()

        if person1 == person2:
            return True

        seen.add(person1)

        for person in person1.adjacent - seen:

            if self.are_connected_recursive(person1, person2, seen)
                return True

        return False










if __name__ == "__main__":

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











    
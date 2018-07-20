"""Find cheapest flights.

Uses Dijkstra's algorithm for weighted path finding.

This is advanced material, and would need to be examined with
help from an algorithms textbook.

joel@joelburton.com
"""


class City(object):
    """City in graph of flights."""

    def __init__(self, name):
        self.name = name
        self.flights = set()

    def __repr__(self):
        return self.name

    def add_flight(self, destination, cost):
        """Add a flight, given a destination and cost."""

        self.flights.add((destination, cost))


class Flights(object):
    """Directed graph of flights."""

    def __init__(self, cities):
        self.cities = cities

    def cheapest(self, src):
        """Find the cheapest path from src to every city.

        Returns dictionary of City: cheapest-path.
        """

        # This uses "Dijkstra's algorithm" 
        # (read about it in a textbook)

        inf = float('inf')   # infinity

        # for each vertex v of the graph, add an entry to the 
        # queue, with the source having distance 0 and all 
        # others having infinite distance

        d = {v: 0 if v is src else inf for v in self.cities}
        queue = {v: (cost, v) for v, cost in d.items()}

        cloud = {}  # map reachable v to its d[v] value

        while queue:
            # Remove the cheapest path from the queue
            # (this won't scale well, as we're constantly 
            # sorting --- better to use a priority queue,
            # at the cost of a little more complexity)
            u_cost, u = queue.pop(sorted(queue.values())[0][1])

            # Note the cost of this
            cloud[u] = u_cost

            for v, v_cost in u.flights:
                # Look for a cheaper way to make this same leg
                if v not in cloud and d[u] + v_cost < d[v]:
                    d[v] = d[u] + v_cost
                    queue[v] = (d[v], v)

        return cloud


atlanta = City("Atlanta")
oakland = City("Oakland")
houston = City("Houston")
la = City("LA")
seattle = City("Seattle")
denver = City("Denver")

flights = Flights([atlanta, oakland, houston, la, seattle, denver])

atlanta.add_flight(oakland, 400)
atlanta.add_flight(houston, 200)
atlanta.add_flight(la, 250)
la.add_flight(oakland, 100)
la.add_flight(seattle, 200)
houston.add_flight(la, 200)
houston.add_flight(denver, 250)
houston.add_flight(oakland, 75)
denver.add_flight(oakland, 150)
denver.add_flight(la, 150)
seattle.add_flight(oakland, 100)

print "Cheapest paths from Atlanta", flights.cheapest(atlanta)

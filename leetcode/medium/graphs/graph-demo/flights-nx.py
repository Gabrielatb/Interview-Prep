"""Find cheapest flights.

Uses NetworkX.
"""

import networkx as nx

G = nx.Graph()

G.add_nodes_from(
    ["Atlanta", "Oakland", "Houston", "LA", "Seattle", "Denver"])

flights = [
    ("Atlanta", "Oakland", 400),
    ("Atlanta", "Houston", 200),
    ("Atlanta", "LA", 250),
    ("LA", "Oakland", 100),
    ("LA", "Seattle", 200),
    ("Houston", "LA", 200),
    ("Houston", "Oakland", 75),
    ("Denver", "Oakland", 150),
    ("Dener", "LA", 150),
    ("Seattle", "Oakland", 100)
]

for src, dest, cost in flights:
    G.add_edge(src, dest, {'weight': cost})

print "Cheapest Atlanta -> Oakland", nx.shortest_path_length(
    G, "Atlanta", "Oakland", "weight")

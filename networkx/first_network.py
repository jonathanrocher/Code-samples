import networkx as nx
# Create a graph
g = nx.Graph()
# Populate the graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
# Create edges
g.add_edge(1,2)
g.add_edge(1,3)
# Print the neighbors of node 1 (returns 2 and 3)
print g.neighbors(1)
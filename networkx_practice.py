import networkx as nx

G = nx.Graph()

G.add_nodes_from([0,1,2,3,4,5,6])
G.add_edges_from([(0,1),(1,2),(2,3),(3,5),(4,5),(5,6)])
print(G.nodes())
print(G.edges())

deg_centrality = nx.degree_centrality(G)
print(deg_centrality)

close_centrality = nx.closeness_centrality(G)
print(close_centrality)

between_centrality = nx.betweenness_centrality(G, normalized=True, endpoints=False)
print(between_centrality)
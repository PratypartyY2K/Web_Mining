import networkx as nx

def betweenness_centrality(G, k=None, normalized=True, weight=None,
						endpoints=False, seed=None):
	betweenness = dict.fromkeys(G, 0.0) # b[v]=0 for v in G
	if k is None:
		nodes = G
	else:
		nx.random.seed(seed)
		nodes = nx.random.sample(G.nodes(), k)
	for s in nodes:

		# single source shortest paths
		if weight is None: # use BFS
			S, P, sigma = nx._single_source_shortest_path_basic(G, s)
		else: # use Dijkstra's algorithm
			S, P, sigma = nx._single_source_dijkstra_path_basic(G, s, weight)

		# accumulation
		if endpoints:
			betweenness = nx._accumulate_endpoints(betweenness, S, P, sigma, s)
		else:
			betweenness = nx._accumulate_basic(betweenness, S, P, sigma, s)

	# rescaling
	betweenness = nx._rescale(betweenness, len(G), normalized=normalized,
						directed=G.is_directed(), k=k)
	return betweenness

G=nx.DiGraph()
G.add_nodes_from([0,6])
edges = [(0,1),(0,2),(0,3),(1,3),(1,4),(2,5),(3,5),(3,6),(4,3),(4,6),(6,5)]
G.add_edges_from(edges)
b=nx.betweenness_centrality(G)
print(b)
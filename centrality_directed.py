#A simple representation of graph using Adjacency Matrix
class Graph:
    def __init__(self,numvertex):
        self.adjMatrix = [[0]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist =[0]*numvertex

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
    
    def get_matrix(self):
        return self.adjMatrix

G = Graph(7)

G.set_vertex(0,1)
G.set_vertex(1,2)
G.set_vertex(2,3)
G.set_vertex(3,4)
G.set_vertex(4,5)
G.set_vertex(5,6)
G.set_vertex(6,7)

G.set_edge(1,4,1)
G.set_edge(1,3,1)
G.set_edge(1,2,1)
G.set_edge(2,4,1)
G.set_edge(2,5,1)
G.set_edge(3,6,1)
G.set_edge(4,3,1)
G.set_edge(4,7,1)
G.set_edge(4,6,1)
G.set_edge(5,4,1)
G.set_edge(5,7,1)
G.set_edge(7,6,1)

def in_degree(matrix):
    indegree = [0]*7
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            indegree[j] = indegree[j] + matrix[i][j]
    
    return indegree

def out_degree(matrix):
    outdegree = [0]*7
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            outdegree[i] = outdegree[i] + matrix[i][j]

    return outdegree

# Degree Centrality
n = 7
graphMatrix = G.get_matrix()
outdegree = out_degree(graphMatrix)
for i in range(len(outdegree)):
    print(f'Degree centrality of node {i+1} is {outdegree[i]}/{n-1}')

# Closeness centrality
from collections import defaultdict

class Graph1:
	def __init__(self,vertices):

		self.V = vertices # No. of vertices

		# dictionary containing adjacency List
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))


	# A recursive function used by shortestPath
	def topologicalSortUtil(self,v,visited,stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		if v in self.graph.keys():
			for node,weight in self.graph[v]:
				if visited[node] == False:
					self.topologicalSortUtil(node,visited,stack)

		# Push current vertex to stack which stores topological sort
		stack.append(v)


	''' The function to find shortest paths from given vertex.
		It uses recursive topologicalSortUtil() to get topological
		sorting of given graph.'''
	def shortestPath(self, s):

		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack =[]

		# Call the recursive helper function to store Topological
		# Sort starting from source vertices
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(s,visited,stack)

		# Initialize distances to all vertices as infinite and
		# distance to source as 0
		dist = [float("Inf")] * (self.V)
		dist[s] = 0

		# Process vertices in topological order
		while stack:

			# Get the next vertex from topological order
			i = stack.pop()

			# Update distances of all adjacent vertices
			for node,weight in self.graph[i]:
				if dist[node] > dist[i] + weight:
					dist[node] = dist[i] + weight

		# Print the calculated shortest distance
		sum_of_distances = 0
		for i in range(self.V):
			# print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")
			if dist[i] == float("Inf"):
				continue
			sum_of_distances += dist[i]
		
		return sum_of_distances


g1 = Graph1(7)
g1.addEdge(0,3,1)
g1.addEdge(0,2,1)
g1.addEdge(0,1,1)
g1.addEdge(1,3,1)
g1.addEdge(1,4,1)
g1.addEdge(2,5,1)
g1.addEdge(3,2,1)
g1.addEdge(3,6,1)
g1.addEdge(3,5,1)
g1.addEdge(4,3,1)
g1.addEdge(4,6,1)
g1.addEdge(6,5,1)

for i in range(7):
	sum_of_node = g1.shortestPath(i)
	if sum_of_node == 0:
		print(f'Closeness centrality of node {i+1} is 0')	
		continue
	print(f'Closeness centrality of node {i+1} is {6/sum_of_node}')

# Betweeness centrality
# Python program for the above approach

# Function to form edge between
# two vertices src and dest
from typing import List
from sys import maxsize
from collections import deque

def add_edge(adj: List[List[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)

# Function which finds all the paths
# and stores it in paths array
def find_paths(paths: List[List[int]], path: List[int],
        parent: List[List[int]], n: int, u: int) -> None:
    # Base Case
    if (u == -1):
        paths.append(path.copy())
        return

    # Loop for all the parents
    # of the given vertex
    for par in parent[u]:

        # Insert the current
        # vertex in path
        path.append(u)

        # Recursive call for its parent
        find_paths(paths, path, parent, n, par)

        # Remove the current vertex
        path.pop()

# Function which performs bfs
# from the given source vertex
def bfs(adj: List[List[int]],
    parent: List[List[int]], n: int,
    start: int) -> None:

    # dist will contain shortest distance
    # from start to every other vertex
    dist = [maxsize for _ in range(n)]
    q = deque()

    # Insert source vertex in queue and make
    # its parent -1 and distance 0
    q.append(start)
    parent[start] = [-1]
    dist[start] = 0

    # Until Queue is empty
    while q:
        u = q[0]
        q.popleft()
        for v in adj[u]:
            if (dist[v] > dist[u] + 1):

                # A shorter distance is found
                # So erase all the previous parents
                # and insert new parent u in parent[v]
                dist[v] = dist[u] + 1
                q.append(v)
                parent[v].clear()
                parent[v].append(u)

            elif (dist[v] == dist[u] + 1):

                # Another candidate parent for
                # shortes path found
                parent[v].append(u)

    # Function which prints all the paths
    # from start to end
def print_paths(adj: List[List[int]], n: int, start: int, end: int) -> None:
    paths = []
    path = []
    parent = [[] for _ in range(n)]
    all_paths = []
    # Function call to bfs
    bfs(adj, parent, n, start)
    # Function call to find_paths
    find_paths(paths, path, parent, n, end)
    for v in paths:

        # Since paths contain each
        # path in reverse order,
        # so reverse it
        v = reversed(v)
        temp_list = []

        # Print node for the current path
        for u in v:
            temp_list.append(u)
        all_paths.append(temp_list[1:(len(temp_list)-1)])
    return all_paths

# Number of vertices
n = 7

# array of vectors is used
# to store the graph
# in the form of an adjacency list
adj = [[] for _ in range(n)]

def matrix_to_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                adj[i].append(j)
    return adj

adj = matrix_to_list(G.get_matrix())

# Given source and destination
# src = 1
# dest = 7
total_betweeness_centrality = [0]*7

for i in range(7):
    for j in range(i,7):
       all_paths = print_paths(adj, n, i, j)
       denominator = len(all_paths)
       unique_node = set()
       for k in range(len(all_paths)):
           for m in range(len(all_paths[0])):
               total_betweeness_centrality[all_paths[k][m]] = total_betweeness_centrality[all_paths[k][m]] + (1/denominator)

for i in range(len(total_betweeness_centrality)):
	total_betweeness_centrality[i] /= 30

print("Total_betweeness centrality = \n",total_betweeness_centrality)
print("Pratyush Kumar 19BCE0506")
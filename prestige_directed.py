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

# Degree Prestige
n = 7
graphMatrix = G.get_matrix()
indegree = in_degree(graphMatrix)
for i in range(len(indegree)):
    print(f'Degree Prestige of node {i+1} is {indegree[i]}/{n-1}')

# Closeness centrality
from collections import defaultdict

class Graph1:
	def __init__(self,vertices):

		self.V = vertices
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
		sum_of_distances = []
		for i in range(self.V):
			# print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")
			sum_of_distances.append(dist[i])

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

a = []

for i in range(7):
	d = g1.shortestPath(i)
	a.append(d)

sumDistance = [0]*7
In = [-1]*7
for i in range(len(a)):
	for j in range(len(a[0])):
		if a[i][j] == float("Inf"):
			continue
		sumDistance[j] = sumDistance[j] + a[i][j]
		In[j] += 1

for d in range(len(sumDistance)):
	if sumDistance[d] == 0:
		print(f'Proximity Prestige of node {d+1} is 0')
		continue
	de = sumDistance[d]/In[d]
	nu = In[d]/6
	print(f'Proximity Prestige of node {d+1} is {nu/de}')

print("19BCE0506 Pratyush Kumar")
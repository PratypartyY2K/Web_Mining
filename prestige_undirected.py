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
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost
    
    def get_matrix(self):
        return self.adjMatrix

G = Graph(16)

G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_vertex(6,'g')
G.set_vertex(7,'h')
G.set_vertex(8,'i')
G.set_vertex(9,'j')
G.set_vertex(10,'k')
G.set_vertex(11,'l')
G.set_vertex(12,'m')
G.set_vertex(13,'n')
G.set_vertex(14,'o')
G.set_vertex(15,'p')

G.set_edge('a','b',1)
G.set_edge('a','e',1)
G.set_edge('a','f',1)
G.set_edge('b','c',1)
G.set_edge('c','d',1)
G.set_edge('c','f',1)
G.set_edge('d','g',1)
G.set_edge('e','i',1)
G.set_edge('f','g',1)
G.set_edge('f','j',1)
G.set_edge('g','h',1)
G.set_edge('g','j',1)
G.set_edge('g','k',1)
G.set_edge('h','l',1)
G.set_edge('h','o',1)
G.set_edge('i','j',1)
G.set_edge('i','n',1)
G.set_edge('i','m',1)
G.set_edge('j','o',1)
G.set_edge('j','n',1)
G.set_edge('k','o',1)
G.set_edge('l','p',1)
G.set_edge('n','o',1)
G.set_edge('o','p',1)

# Degree Centrality
n = 16
graphMatrix = G.get_matrix()
for i in range (len(graphMatrix)):
    no_of_edges = 0
    for j in range(len(graphMatrix[i])):
        if graphMatrix[i][j] == 1:
            no_of_edges += 1
    print(f'Degree Prestige of node {chr(97 + i)} is {no_of_edges}/{n-1}')

# Closeness centrality
import sys

class Graph1():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(chr(node + 97), "\t", dist[node])

    def get_sum_shortest_path(self, dist):
        sum_of_path = 0
        for node in range(self.V):
            sum_of_path = sum_of_path + dist[node]
        return sum_of_path

    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        # self.printSolution(dist)
        return self.get_sum_shortest_path(dist)

# Driver program
g1 = Graph1(16)
g1.graph = G.get_matrix()

for i in range(len(g1.graph)):
    sum_of_node = g1.dijkstra(i)
    print(f'Proximity prestige of node {chr(97 + i)} is {15/sum_of_node}')

print("19BCE0506 Pratyush Kumar")
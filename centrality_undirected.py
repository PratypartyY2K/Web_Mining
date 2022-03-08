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
    print(f'Degree centrality of node {chr(97 + i)} is {no_of_edges}/{n-1}')

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
    print(f'Closeness centrality of node {chr(97 + i)} is {15/sum_of_node}')


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
        #all_paths.append(v)

        temp_list = []

        # Print node for the current path
        for u in v:
            temp_list.append(u)

        all_paths.append(temp_list[1:(len(temp_list)-1)])
    return all_paths



# Number of vertices
n = 16

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
total_betweeness_centrality = [0]*16

for i in range(16):
    for j in range(i,16):
       all_paths = print_paths(adj, n, i, j)
       denominator = len(all_paths)
       unique_node = set()
       for k in range(len(all_paths)):
           for m in range(len(all_paths[0])):
               total_betweeness_centrality[all_paths[k][m]] = total_betweeness_centrality[all_paths[k][m]] + (1/denominator)

for i in range(len(total_betweeness_centrality)):
	total_betweeness_centrality[i] /= 105

print("Betweeness centrality = ", total_betweeness_centrality)
print("19CBE0506 Pratyush Kumar")
# Step1 : Convert the directed graph into a adjacency matrix
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

n = 6 # number of nodes
G = Graph(n)

def out_degree(matrix):
    outdegree = [0]*6
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            outdegree[i] = outdegree[i] + matrix[i][j]

    return outdegree

G.set_vertex(0,1)
G.set_vertex(1,2)
G.set_vertex(2,3)
G.set_vertex(3,4)
G.set_vertex(4,5)
G.set_vertex(5,6)

G.set_edge(1,2,1)
G.set_edge(1,3,1)
G.set_edge(3,1,1)
G.set_edge(3,5,1)
G.set_edge(3,2,1)
G.set_edge(4,5,1)
G.set_edge(4,6,1)
G.set_edge(5,6,1)
G.set_edge(5,4,1)
G.set_edge(6,4,1)

# first iteration, give page rank to each node 1/n
# create a dictionary for each node
old_pg = [1/n]*6

# number of iterations is 7
# first iteration is done
# page rank of node 'i' = sum (page rank in prev itr/number of outlinks)
# jis jis nodes se ith node receive hota hai unpar formula use karna
adj_mat = G.get_matrix()
outdegree = out_degree(adj_mat)
outdegree_norm=[0]*6
for i in range(len(outdegree)):
    if outdegree[i] == 0:
        outdegree_norm[i] = 0
    else:
        outdegree_norm[i] = 1/outdegree[i]

adj = [[] for _ in range(n)]

def matrix_to_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                adj[j].append(i)
    return adj

adj = matrix_to_list(G.get_matrix())
#print(adj)

for i in range(7):
    new_old_pg = [0]*6
    for j in range(len(adj)):
        sum_pg = 0
        #print(adj[j])
        for k in adj[j]:
            #print(i)
            #print(old_pg[k])
            #print(outdegree_norm[k-1])
            temp = old_pg[k] * outdegree_norm[k]
            sum_pg += temp
        new_old_pg[j] = sum_pg
    print(f'Iteration {i+1}')
    print(new_old_pg)
    old_pg = new_old_pg

page_rank = {}
for i in range(1,7):
    page_rank[i] = old_pg[i-1]
sorted_page_rank = {k: v for k, v in sorted(page_rank.items(), key = lambda item: item[1])}
index = list(sorted_page_rank.items())
print("Fnial iteration results = ", sorted_page_rank)
for i in range(len(index)):
    print(f'Page rank {i+1} is for node {index[i]}')
print("19BCE0506 Pratyush Kumar")
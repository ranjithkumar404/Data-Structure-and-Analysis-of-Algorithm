import sys

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Thermal station ---- connected to ---> Thermal cost")
        for i in range(1, self.v):
            print(f"   {i}--   {parent[i]}   {self.graph[i][parent[i]]}")

    def prim_mst(self):
        key = [sys.maxsize] * self.v
        key[0] = 0
        mst_set = [False] * self.v
        parent = [-1] * self.v

        for _ in range(self.v):
            min_key = sys.maxsize
            min_index = 0

            for v in range(self.v):
                if key[v] < min_key and not mst_set[v]:
                    min_key = key[v]
                    min_index = v

            mst_set[min_index] = True
            for v in range(self.v):
                if self.graph[min_index][v] > 0 and not mst_set[v] and self.graph[min_index][v] < key[v]:
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index

        self.print_mst(parent)

# Accepting user input
n = int(input("Enter the number of thermal power stations: "))
g = Graph(n)

print("Enter the cost for electrification of each connection:")
for i in range(n):
    for j in range(i + 1, n):
        cost = int(input(f"Enter the cost between thermal station {i} and {j}: "))
        g.add_edge(i, j, cost)

# Compute and display the minimum cost connections
g.prim_mst()

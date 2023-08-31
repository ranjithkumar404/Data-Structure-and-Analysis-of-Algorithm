import heapq
def dijkstra(graph,start):
  distances={node:float('inf') for node in graph}
  distances[start]=0
  heap=[(0,start)]

  while heap:
    cd,cn=heapq.heappop(heap)
    if cd > distances[cn]:
      continue

    for n,w in graph[cn].items():
      distance=cd+w
      if distance < distances[n]:
        distances[n]=distance
        heapq.heappush(heap,(distance,n))

  return distances

def optimal(graph,start,dest):
  distances=dijkstra(graph,start)
  if distances[dest]==float('inf'):
    return None
  node=dest
  route=[]

  while node !=start:
    route.append(node)
    neighbours=graph[node]
    min=float('inf')
    nn=None
    for n,w in neighbours.items():
      if distances[n]+w==distances[node] and distances[n] <min:
        min=distances[n]
        nn=n
    if nn is None or nn in route:
      return None
    node=nn

  route.append(start)
  route.reverse()
  return route


# n=int(input("Enter the no.of nodes"))
# graph={}
# for i in range(n):
#   node=input("Enter the node name")
#   m=int(input(f"Enter the no.of nodes connected to {node}"))
#   graph[node]={}
#   for j in range(m):
#     node1=input(f"Enter the node connected to {node}")
#     d=int(input(f"Enter the distance from {node } to {node1}"))
#     graph[node][node1]=d
graph = {
    'A': {'B': 3, 'C': 99, 'D': 7, 'E': 99},
    'B': {'A': 3, 'C': 4, 'D': 2, 'E': 99},
    'C': {'A': 99, 'B': 4, 'D': 5, 'E': 6},
    'D': {'A': 7, 'B': 2, 'C': 5, 'E': 4},
    'E': {'A': 99, 'B': 99, 'C': 6, 'D': 4}
}
start=input("Enter the start node")
dest=input("enter the destination")
x=optimal(graph,start,dest)
if x is None:
  print("No optimal routes")
else:
  print("the optimal route is ","->".join(x))

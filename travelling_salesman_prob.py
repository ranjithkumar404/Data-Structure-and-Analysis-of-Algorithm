import networkx as nx
def distances(n):
  distances={}
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      d=int(input(f"Enter the distance between {i} and {j}"))
      distances[(i,j)]=d
      distances[(j,i)]=d

  return distances

def tsp(distances):
  G=nx.Graph()
  G.add_weighted_edges_from((i,j,d)  for(i,j),d in distances.items() )
  order=nx.approximation.traveling_salesman_problem(G,cycle=True)
  return order

def cost(distances,order):
  total=sum(distances[(order[i],order[i+1])] for i in range(len(order)-1))
  return total

n=int(input("Enter the total number of nodes"))
d=distances(n)
order=tsp(d)
cost=cost(d,order)
print("The order is",order)
print("The cost is",cost)

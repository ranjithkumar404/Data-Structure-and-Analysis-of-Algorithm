def knapsack(weight,cost,c):
  n=len(weight)
  table=[[0]*(c+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,c+1):
      if weight[i-1]<=j:
        table[i][j]=max(cost[i-1]+table[i-1][j-weight[i-1]],table[i-1][j])
      else:
        table[i][j]=table[i-1][j]

  solution=[]
  total=c
  for i in range(n,0,-1):
    if table[i][total]!=table[i-1][total]:
      solution.append(i-1)
      total-=weight[i-1]
  return table[n][c],solution

n=int(input("Enter the total number of items"))
w=[]
c=[]
for i in range(n):
  w1=int(input(f"Enter the weight of item{i+1}"))
  w.append(w1)
for i in range(n):
  w1=int(input(f"Enter the cost of item{i+1}"))
  c.append(w1)
ca=int(input("enter the capacity"))
soln,total=knapsack(w,c,ca)
print("the total profit is",total)
print("selected items",soln)
print("selected weights",[w[i] for i in soln])

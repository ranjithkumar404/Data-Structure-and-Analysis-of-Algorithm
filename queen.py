def safe(b,r,c,n):
  for i in range(r):
    if b[i][c]==1:
      return False
    if c-r+i >=0 and b[i][c-r+i]==1:
      return False
    if c+r-i < n and b[i][c+r-i]==1:
      return False
  return True

def solve(n):
  solution=[]
  def backtrack(r):
    if r==n:
      solution.append([''.join('Q' if c==1 else '.' for c in r)for r in b])
      return
    for c in range(n):
      if safe(b,r,c,n):
        b[r][c]=1
        backtrack(r+1)
        b[r][c]=0

  b=[[0]*n for _ in  range(n)]
  backtrack(0)
  return solution


n=int(input("enter the value for n"))

s=solve(n)
for i in s:
  for r in i:
    print(r)
  print()

class Job:
  def __init__(self,p,d,id):
    self.id=id
    self.p=p
    self.d=d

def schedule(jobs,T):
  p=0
  slot=[-1]*T
  jobs.sort(key=lambda x:x.p,reverse=True )
  for job in jobs:
    for i in reversed(range(job.d)) :
      if i<T and slot[i]==-1:
        p+=job.p
        slot[i]=job.id
        break
  print("The selected jobs are",list(filter(lambda x:x!=-1,slot)))
  print("The total profit is",p)
n=int(input("Enter the number of jobs"))
jobs=[]
for i in range(n):
  id=int(input(f"Enter the id for job{i+1}"))
  d=int(input("Enter the deadline"))
  p=int(input("Enter the profit"))
  jobs.append(Job(p,d,id))
t=int(input("Enter the value for T"))
schedule(jobs,t)

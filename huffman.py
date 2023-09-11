import heapq
class Node:
  def __init__(self,f,s,l=None,r=None):
    self.f=f
    self.s=s
    self.l=l
    self.r=r
    self.huff=' '

  def __lt__(self,nxt):
    return self.f < nxt.f

def encoded(text, huffman_tree):
    encoding_map = {}

    def traverse_tree(node, code=''):
        if node.l:
            traverse_tree(node.l, code + '0')
        if node.r:
            traverse_tree(node.r, code + '1')
        if not node.l and not node.r:
            encoding_map[node.s] = code

    traverse_tree(huffman_tree)

    encoded_text = ''
    for char in text:
        encoded_text += encoding_map[char]

    return encoded_text

def decoded(txt,h):
  d=''
  cn=h
  for b in txt:
    if b=='0':
      cn=cn.l
    else:
      cn=cn.r
    if not cn.l and not cn.r:
      d+=cn.s
      cn=h
  return d
def printt(node, val=''):
    newVal = val + str(node.huff)
    if node.l:
        printt(node.l, newVal)
    if node.r:
        printt(node.r, newVal)
    if not node.l and not node.r:
        print(f"{node.s} -> {newVal}")


char=input("Enter the characters").split(' ')
f=[int (i) for i in input("Enter the frequency").split(' ')]

nodes=[]
for i in range(len(char)):
  heapq.heappush(nodes,Node(f[i],char[i]))
while len(nodes)>1:
  l=heapq.heappop(nodes)
  r=heapq.heappop(nodes)
  l.huff=0
  r.huff=1
  nn=Node(l.f+r.f,l.s+r.s,l,r)
  heapq.heappush(nodes,nn)
printt(nodes[0])
h=nodes[0]
txt1=input("Enter the text to decode")
ans1=decoded(txt1,h)
print(f"decoded text is {ans1}")
txt2=input("enter the text to encode")
ans2=encoded(txt2,h)
print(f"Encoded text is {ans2}")

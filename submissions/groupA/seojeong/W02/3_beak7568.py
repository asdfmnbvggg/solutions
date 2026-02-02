import sys

n=int(sys.stdin.readline())
    
p=[]

for i in range(n):
    w, h = map(int,sys.stdin.readline().split())
    p.append((w, h))

r=[]
    
for i in range(n):
    a=1
    for j in range(n):
        if p[j][0]>p[i][0] and p[j][1]>p[i][1]:
            a+=1
    r.append(a)

for i in r:
    print(i, end=' ')
import sys

num = list(map(int,sys.stdin.readline().split()))
m = list(map(int,sys.stdin.readline().split()))
sum_n = 0

for i in m:
    n = m.copy()
    n.remove(i)
    for j in n :
        k = n.copy()
        k.remove(j)
        for l in k :
            if i+j+l <= num[1]:
                if sum_n <= i+j+l :
                    sum_n = i+j+l
                    
print(sum_n)
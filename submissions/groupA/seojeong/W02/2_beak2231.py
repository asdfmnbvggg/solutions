import sys

n=int(sys.stdin.readline().strip())

sub=max(1,n-len(str(n))*9)

def each_sum(num):
    i=0
    while True:
        i+=num%10
        num=num//10
        if num==0 : break
    return i



for i in range(sub,n):
    sum_n=i+each_sum(i)
    if sum_n == n:
        print(i)
        break
else : print(0)
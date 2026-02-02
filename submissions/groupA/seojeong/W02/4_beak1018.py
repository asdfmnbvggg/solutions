import sys

n,m=map(int,sys.stdin.readline().split())

#각 줄 2D array로 받기
b = []
for i in range(n):
    c = [] #list c는 계속 초기화하고 b에 누적
    wb = sys.stdin.readline().strip()
    for WB in wb:
        c.append(WB)
    b.append(c)
    
#수정하더라도 최대 64개까지 수정할 수가 있음
min_c=64

#시작지점 받기
for i in range(n-7):
    for j in range(m-7):
        fix_a=0
        fix_b=0
        
        for k in range(8):
            for l in range(8):
                check = b[i+k][j+l] #시작지점부터 8*8 사이즈 확인하기 위해 값 받기

                if (k + l) % 2 == 0: 
                    if check != 'W': #어떤 것을 바꾸는게 더 작은 경우의 수인지 알기 위해 나누어줌
                        fix_a += 1  
                    if check != 'B':
                        fix_b += 1  
                else:
                    if check != 'B':
                        fix_a += 1
                    if check != 'W':
                        fix_b += 1
                        
        min_c=min(min_c,fix_a,fix_b)
                        
print(min_c)
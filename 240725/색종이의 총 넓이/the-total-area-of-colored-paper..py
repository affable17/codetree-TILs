OFFSET = 100
N = int(input())
arr =[[0 for _ in range(201)] for _ in range(201)] 


for _ in range(N):
    x , y = map(int, input().split()) #좌측하단 꼭지
    x += OFFSET
    y += OFFSET

    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j]=1

cnt=0
for i in range(201):
    for j in range(201):
        if arr[i][j]==1:
            cnt+=1

print(cnt)
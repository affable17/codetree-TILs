n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    global n
    if x>=0 and x<n and y>=0 and y<n:
        return True
#상하좌우
dxs=[-1, 1, 0, 0]
dys=[0, 0, -1, 1]
x, y =0, 0

ans =0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx , ny = x + dx, y +dy
            if in_range(nx, ny) and graph[nx][ny]==1:
                cnt+=1
        if cnt >= 3:
            ans+=1

print(ans)
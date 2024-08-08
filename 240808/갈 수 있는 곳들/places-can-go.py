from collections import deque


n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)] #0은 이동 가능 1은 불가능
visited = [[0 for _ in range(n)] for _ in range(n)]


q = deque()
start_points = []
#k개의 시작점
for _ in range(k):
    x, y = tuple(map(int, input().split())) #주어지는 것이 row/col, 인덱스가 아님
    q.append((x-1, y-1))
    visited[x-1][y-1] =1


#상하좌우 
dxs = [-1, 1, 0 , 0]
dys = [0, 0, -1 ,1]


def in_range(x,y):
    global n
    if x >=0 and x<n and y>=0 and y<n:
        return True

def can_go(x,y):
    if in_range(x,y) and not visited[x][y] and grid[x][y]==0:
        return True 
 

def bfs():
    global cnt 
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y]=1
             

bfs()
ans =0
for i in range(n):
    for j in range(n):
        if visited[i][j]==1:
            ans +=1

print(ans)
from collections import deque
queue = deque()

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

#아래/오른쪽/좌/위
dxs =[-1, 0, 0, 1]
dys =[0, 1, -1, 0]
def inRange(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True

def can_go(x, y):
    if not inRange(x,y):
        return False
    if visited[x][y] or grid[x][y]==0:
        return False
    return True

def bfs(x, y):

    while queue:
        x , y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y+ dy
            if can_go(new_x,new_y):
                queue.append((new_x,new_y))
                visited[new_x][new_y]=1
            
queue.append((0,0))
visited[0][0]= 1

bfs(0,0)

print(visited[n-1][m-1])
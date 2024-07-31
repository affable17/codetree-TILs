n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

#아래/오른쪽
dxs = [1, 0]
dys = [0, 1]

x,y = 0 ,0
def inRange(x,y):
    return x>=0 and x<n and y>=0 and y<n
def can_go(x,y):
    if not inRange(x,y):
        return False
    #뱀이 있으면 0, 뱀이 없으면 1
    if visited[x][y]==1 or graph[x][y] == 0:
        return False
    return True


def dfs(x , y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = dx + x, dy+ y
        if can_go(new_x, new_y):
            visited[new_x][new_y]=1
            dfs(new_x, new_y)


visited[0][0]=1
dfs(0,0)

print(visited[n-1][n-1])
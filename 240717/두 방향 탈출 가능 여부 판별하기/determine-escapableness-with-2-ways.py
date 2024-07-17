n, m = map(int, input().split())

#뱀이 있으면 : 0, 뱀이 없으면 : 1
grid =[
    list(map(int, input().split())) for _ in range(n)
]

visited = [
    [0 for _ in range(m)] for _ in range(n)
]

def in_range(x,y): #격자에서 벗어나지 않기
    if (x >=0) and (x < n) and (y>=0) and (y < m):
        return True

def can_go(x,y): #이동 가능한지 확인
    if not in_range(x,y):
        return False
    if visited[x][y]==1 or grid[x][y]==0:
        return False #갈 수 없는 경우

    return True #default는 갈 수 있다. 

def dfs(x , y):
    
    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy 

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1 #간걸로 표시
            dfs(new_x, new_y)

# x=0, y=0에서 시작
visited[0][0]=1
dfs(0,0)

#도착했는지 확인
print(visited[-1][-1])
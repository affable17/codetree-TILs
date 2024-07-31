n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0for _ in range(m)] for _ in range(n)]
num = 1
graph[0][0]=1
visited[0][0]=1
x , y = 0, 0

#오/아래/왼/위
dxs =[0, +1, 0, -1]
dys =[1, 0 , -1 ,0]

def in_Range(x ,y):
    if x>=0 and x < n and y>=0 and y<m:
        return True

direc = 0
for i in range(n*m-1):
    
    new_x, new_y = x + dxs[direc%4], y+dys[direc%4]
    
    if in_Range(new_x,new_y) and not visited[new_x][new_y]: #범위 내에 있고, 방문하지 않았다면
        x, y = new_x, new_y
    else: #범위를 벗어나거나 방문을 하였다면
        direc +=1
        x, y = x + dxs[direc%4], y+ dys[direc%4]
    
    num+=1
    visited[x][y]= 1
    graph[x][y]= num

for row in graph:
    for col in row:
        print(col, end=" ")
    print()
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
cnt =0

for _ in range(e):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(v):
    global cnt
    for curr_v in graph[v]:
        if not visited[curr_v]: 
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)
    return cnt 

visited[1] = True
print(dfs(1))
N, M = map(int, input().split())

#인접리스트 만들기 (graph) N개의 정점
graph = [[]for _ in range(N+1)]

#방문 확인
visited = [False for _ in range(N+1)]
vertex_cnt = 0

def dfs(v):
    global vertex_cnt

    for curr_v in graph[v]:
        if not visited[curr_v]:
            visited[curr_v]=True
            vertex_cnt+=1
            dfs(v)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1]=True
dfs(1)

print(graph)
print(vertex_cnt)
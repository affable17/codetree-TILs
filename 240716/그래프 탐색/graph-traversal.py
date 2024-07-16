N, M = map(int, input().split()) #N정점 M간선

graph = [[] for _ in range(N+1)] #idx는 0부터 인거 고려해서 0~N 까지 

visited =[False for _ in range(N+1)]
vertex_cnt = 0


#인접리스트 그래프 
for _ in range(M):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

#curr_v == current vertex
def dfs(v): # v for vertex
    global vertex_cnt
    for curr_v in graph[v]:

        if not visited[curr_v]:
            visited[curr_v]=True
            vertex_cnt += 1
            dfs(curr_v)


root_vertex =1
visited[root_vertex]=True

dfs(root_vertex)
print(vertex_cnt)
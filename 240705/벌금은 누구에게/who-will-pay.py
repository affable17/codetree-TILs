N, M, K = map(int, input().split())

arr = [0]*(N+1)

for _ in range(M):
    student = int(input())
    arr[student]+=1
    if arr[student] >= K:
        print(student)
        break
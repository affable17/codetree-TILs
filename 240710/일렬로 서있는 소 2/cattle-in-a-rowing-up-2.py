N = int(input())
arr = list(map(int, input().split()))

cnt=0
for i in range(N): # i: 0~4
    for j in range(i+1,N): #j: i+1 ~ 5
        for k in range(j+1, N):
            if arr[i]<=arr[j] and arr[j]<=arr[k]:
                cnt+=1
print(cnt)
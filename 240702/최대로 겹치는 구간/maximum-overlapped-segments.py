N = int(input())
arr =[0]*200

for _ in range(N):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        arr[i]+=1

print(max(arr))
n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_num=0
for i in range(n-k+1):
    sum = 0
    for j in range(i, i+k):
        sum += arr[j]
        max_num = max(max_num, sum)
        print(i, max_num)


print(max_num)
import sys
N = int(input())
arr = list(map(int, input().split()))
x = sys.maxsize

for i in range(N):
    sum = 0
    for j in range(N):
        sum+=arr[j] * abs(i-j) #사람수 * 거리
    if sum < x:
        x = sum #new min 
print(x)
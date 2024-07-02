import sys
N, K = map(int, input().split())
arr = [0]*N

for _ in range(K):
    A, B = map(int, input().split())
    for i in range(A, B+1):
        arr[i-1] +=1

#배열에서 최댓값 찾기
num = -sys.maxsize
for k in arr:
    if k >= num:
        num = k 
print(num)
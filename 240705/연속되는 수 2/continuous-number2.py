N = int(input())
arr =[]



for _ in range(N):
    arr.append(int(input()))

max_num =0 
arr2 =[]

for i in range(N):
    if i==0:
        cnt = 1
    elif arr[i]!=arr[i-1]: #수열 원소가 바뀐다면
        arr2.append(cnt)
        cnt = 1
    else:
        cnt +=1

arr2.append(cnt)
print(max(arr2))
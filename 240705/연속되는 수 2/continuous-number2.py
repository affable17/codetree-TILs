N = int(input())
arr =[]



for _ in range(N):
    arr.append(int(input()))

max_num =0 
cnt = 0
for i in range(N):
    if i==0 or arr[i]!=arr[i-1]: #수열 원소가 바뀐다면
        if cnt >= max_num:
            max_num = cnt
        cnt = 1
    else:
        cnt +=1

print(max_num)
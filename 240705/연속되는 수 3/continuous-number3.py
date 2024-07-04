N = int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

ans =0
for i in range(N):
    
    if i ==0:
        cnt =1
    elif arr[i]*arr[i-1]>0:
        cnt+=1
    else:
        cnt=1
    ans = max(ans, cnt)
print(ans)
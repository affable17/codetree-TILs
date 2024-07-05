INT_MAX = 1000000
n, m = map(int, input().split())
A =[0]
B =[0]

cur=0
for _ in range(n):
    cmd = input().split()
    t, direction = int(cmd[0]), cmd[1]

    for i in range(1, t+1):
        if direction=='R':
            cur+=1
        else:
            cur-=1
        A.append(cur)

cur2=0
for _ in range(m):
    cmd = input().split()
    t, direction = int(cmd[0]), cmd[1]

    for i in range(1, t+1):
        if direction=='R':
            cur2+=1
        else:
            cur2-=1
        B.append(cur2)


cnt=0
shortest = min(len(A), len(B))
same = 0
for i in range(1, shortest):
    if same==0 and A[i]==B[i]:
        cnt+=1
        same = 1
    else:
        same = 0
print(cnt)
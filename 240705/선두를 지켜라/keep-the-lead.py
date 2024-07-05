N, M = map(int, input().split())

A =[0]
B =[0]

cur = 0
for _ in range(N):
    v, t = map(int, input().split())
    
    for i in range(1, t+1):
        cur = cur + v
        A.append(cur)

cur2=0
for _ in range(M):
    v, t = map(int, input().split())

    for i in range(1, t+1):
        cur2 = cur2 + v
        B.append(cur2)

#선두 찾기
if A[1] > B[1]:
    fast = 'A'
else:
    fast = 'B'


cnt=0
for i in range(2, len(A)): #2시간 부터 확인
    if fast =='A':
        if B[i] > A[i]:
            cnt+=1
            fast = 'B'
    else:
        if A[i] > B[i]:
            cnt+=1
            fast = 'A'

print(cnt)
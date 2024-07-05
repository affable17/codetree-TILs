N, M = map(int, input().split())

A=[0]
B=[0]
cur=0

for _ in range(N):
    x = input().split()
    d, t = x[0], int(x[1]) #direction #time
        
   
    for i in range(1, t+1):
        if d=='R':
            cur += 1     
            A.append(cur)
        else:
            cur -= 1
            A.append(cur)     

            
cur2=0
for _ in range(M):
    x = input().split()
    d, t = x[0], int(x[1])

    for i in range(1, t+1):
        if d=='R':
            cur2+=1
            B.append(cur2)
        else:
            cur2-=1
            B.append(cur2)   

ans=-1
for i in range(1, len(A)):
    if A[i]==B[i]:
        ans=i
        break
print(ans)
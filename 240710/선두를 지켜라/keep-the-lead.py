MAX_T = 1000000
#위치 배열 
pos_A=[0]* MAX_T
pos_B=[0]* MAX_T

N, M = map(int, input().split())


time_A = 1
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_A[time_A] = pos_A[time_A - 1] + v
        time_A += 1


time_B= 1
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_B[time_B] = pos_B[time_B - 1] + v
        time_B += 1

cnt = 0
leader = 0
#A는 1, B는 2
for i in range(1, time_A+1):
    
    if pos_A[i] > pos_B[i]: 
        if leader ==2:
            cnt +=1        
        leader =1       
    elif pos_A[i]<pos_B[i]:
        if leader==1:
            cnt+=1
        leader =2

print(cnt)
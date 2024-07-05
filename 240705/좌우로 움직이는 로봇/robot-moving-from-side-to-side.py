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

#더 길이가 긴 수열 찾기 
if len(A)>len(B):
    longest = A
    shortest = B
else:
    longest = B
    shortest = A



cnt=0
same = 0
for i in range(1, len(longest)):
    val2 = longest[i]

    if i>=(len(shortest)-1):
        val1 = shortest[-1]
    else:
        val1 = shortest[i]
    
    if val1==val2:
        if same == 0:
            cnt+=1
        same = 1
    else:
        same=0
    print(f"i={i}, same={same}, cnt={cnt}")

print(cnt)
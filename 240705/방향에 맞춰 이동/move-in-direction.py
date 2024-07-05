N = int(input())

x, y = 0, 0
#E, W, S, N 순으로 
dx = [1,-1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    cmd = input().split()
    for _ in range(int(cmd[1])):
        if cmd[0]=='E':
            x, y = x+dx[0], y+dy[0]
        elif cmd[0]=='W':
            x, y = x+dx[1], y+dy[1]
        elif cmd[0] =='S':
            x, y = x+dx[2], y+dy[2]
        else:
            x, y = x+dx[3], y+dy[3]
print(x,y)
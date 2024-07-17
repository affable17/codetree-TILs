cmd = input()

x, y = 0 , 0
curr_dir = 3 #현재 북


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(len(cmd)):
    if cmd[i]=='L': #왼쪽으로 방향 바꾸기
        curr_dir = (curr_dir+4-1)%4
    elif cmd[i]=='R': #오르쪽으로 방향 바꾸기
        curr_dir = (curr_dir+1)%4
    elif cmd[i]=='F':
        x , y = x + dx[curr_dir], y + dy[curr_dir]

print(x,y)
n, t = map(int, input().split())
r, c, d = input().split()

r = int(r) #row
c = int(c) #column

direction = {'U': 0, 'L': 1,'R': 2,'D': 3}
dir_num = direction[d]

#상/좌/우/하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1 , 0]
x, y = r, c

def in_range(x,y):
    global n
    if x>=1 and x<=n and y>=1 and y<=n:
        return True

for _ in range(t):
    nx , ny = x + dxs[dir_num], y+ dys[dir_num]
    if in_range(nx, ny):
        x , y = nx , ny
    else:
        dir_num = 3 - dir_num 
print(x,y)
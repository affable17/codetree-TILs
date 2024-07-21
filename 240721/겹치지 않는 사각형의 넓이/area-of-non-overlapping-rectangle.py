MAX_R = 2000
OFFSET = 1000

area=0
arr =[[0]* (MAX_R+1) for _ in range(MAX_R+1)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1 , y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET
    for row in range(x1, x2):
        for col in range(y1, y2):
            arr[row][col]=1

#직사각형 M
x1, y1, x2, y2 = map(int, input().split())
x1 , y1 = x1+OFFSET, y1+OFFSET
x2, y2 = x2+OFFSET, y2+OFFSET
for row in range(x1, x2):
    for col in range(y1, y2):
        arr[row][col]=0
#넓이 구하기 
for row in range(0,MAX_R+1):
    for col in range(0, MAX_R+1):
        if arr[row][col]==1:
            area+=1

print(area)
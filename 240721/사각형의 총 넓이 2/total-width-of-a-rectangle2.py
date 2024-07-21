OFFSET = 100
N= int(input())

area=0

arr = [
    [0] * (201) 
    for _ in range(201)
    ] 


for _ in range(N):
    x1 , y1, x2, y2 = map(int, input().split()) 

    
    x1+=OFFSET
    x2+=OFFSET
    y1+=OFFSET
    y2+=OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j]=1

for row in range(0, 201):
    for col in range(0, 201):
        if arr[row][col]==1:
            area+=1
print(area)
N = int(input())

dots =[]

for _ in range(N):
    dot = tuple(map(int, input().split()))
    dots.append(dot)


area=[]

for i in range(N):
    x_arr =[]
    y_arr =[]
    for j in range(N):
        if j==i:
            continue
        else:
            x, y = dots[j]
            x_arr.append(x)
            y_arr.append(y)
    x_len = max(x_arr)-min(x_arr)
    y_len = max(y_arr)-min(y_arr)
    area.append(x_len*y_len)

print(min(area))
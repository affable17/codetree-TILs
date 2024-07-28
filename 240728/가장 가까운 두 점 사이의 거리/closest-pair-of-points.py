N = int(input())
dots = []

for _ in range(N):
    dot = tuple(map(int, input().split()))
    dots.append(dot)

arr =[]

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = dots[i]
        x2, y2 = dots[j]
        k = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
        arr.append(k)
print(min(arr))
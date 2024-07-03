OFFSET = 100

N = int(input())
seq =[]
array = [0]* 2001
cur =0

for _ in range(N):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'R':
        left_sequence = cur
        right_sequence= cur + distance
        cur += distance
    else:
        left_sequence = cur - distance
        right_sequence = cur
        cur -= distance
    
    seq.append([left_sequence, right_sequence])   

for x1, x2 in seq:
    x1 += OFFSET
    x2 += OFFSET

    for i in range(x1, x2):
        array[i] += 1

cnt =0
for elem in array:
    if elem >= 2:
        cnt +=1
print(cnt)
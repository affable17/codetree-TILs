N, B = map(int, input().split())
ans =[]
while True:
    if N < B:
        ans.append(N)
        break
    ans.append(N % B)
    N = N // B
for d in ans[::-1]:
    print(d, end='')
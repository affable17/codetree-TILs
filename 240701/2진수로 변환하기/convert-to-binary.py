n = int(input())
digits =[]

while (1):
    if n<=1:
        digits.append(n)
        break
    digits.append(n%2)
    n = n//2


for d in digits[::-1]:
    print(d,end=' ')
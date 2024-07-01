a, b = map(int, input().split())
n = input()

#10진수로 바꿔주기
num=0
for i in range(len(n)):
    num = num * a + int(n[i])

#b진수로 바꾸기
digits=[]
while True:
    if num < b:
        digits.append(num)
        break
    digits.append(num%b)
    num //= b

for d in digits[::-1]:
    print(d, end='')
N = input() #이진수 


#십진수로 바꾸기
num=0
for i in range(len(N)):
    num = num * 2 + int(N[i])

#17배 하기
num = num * 17

#이진수로 나타내기
Binary =[]
while True:
    if num < 2:
        Binary.append(num)
        break
    Binary.append(num % 2)
    num = num // 2

for b in Binary[::-1]:
    print(b, end='')
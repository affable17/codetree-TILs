binary = list(map(int, input().split()))
num=0 #10진수
for i in range(len(binary)):
    num = 2 * num + binary[i]
print(num)
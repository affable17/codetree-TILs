N = int(input())

def rec_num(n):
    if n < 10:
        return n**2
    return rec_num(n//10) + (n%10)**2

print(rec_num(N))
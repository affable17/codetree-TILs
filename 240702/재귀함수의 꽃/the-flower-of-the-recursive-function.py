N = int(input())

def rec_func(n):
    if n == 0:
        return 
    print(n, end =' ')
    rec_func(n-1)
    print(n, end =' ')
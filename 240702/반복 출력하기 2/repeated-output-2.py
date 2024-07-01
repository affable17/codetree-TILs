N = int(input())

def print_hw(n):
    if n == 0:
        return 

    print_hw(n-1)
    print("HelloWorld")

print_hw(N)
import sys
input = sys.stdin.readline

def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1

N = int(input())
print(my_factorial(N))
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    str_list = sys.stdin.readline().rstrip().split()
    for word in str_list:
        print(word[::-1], end=" ")
    print()
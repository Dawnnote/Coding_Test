import sys
input = sys.stdin.readline

def dfs(n):
    if n == M:
        print(*num)
        return
    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True
            num.append(i)
            dfs(n+1)
            
            check[i] = False
            num.pop()

N, M = map(int, input().split())

num = []
check = [False] * (N+1)

dfs(0)

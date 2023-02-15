import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cnt = [0] * 1000001
for i in A:
    cnt[i] += 1

stack = []
result = [-1] * N
for i in range(N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(" ".join(map(str, result)))
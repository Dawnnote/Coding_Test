from collections import deque

N, K = map(int, input().split())

deq = deque([i+1 for i in range(N)])
lis = []

for _ in range(N):
  deq.rotate(-K)
  lis.append(deq.pop())

print('<' + str(lis)[1:-1] + '>')
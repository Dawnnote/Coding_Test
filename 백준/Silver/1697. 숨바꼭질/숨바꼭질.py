from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
MAX = 10**5
time = [0]*(MAX+1)

while q:
    num = q.popleft()
    if num == K:
        print(time[num])
        break
    
    for idx in (num-1, num+1, num*2):
        if 0 <= idx <= MAX and not time[idx]:
            time[idx] = time[num] + 1
            q.append(idx)
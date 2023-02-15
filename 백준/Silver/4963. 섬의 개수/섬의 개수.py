from collections import deque
import sys

def bfs(a, b):
    mx = [-1, 1, 0, 0, -1, -1, 1, 1]
    my = [0, 0 ,-1, 1, -1, 1, -1, 1]
    
    q = deque([(a, b)])
    MAP[a][b] = 2
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + mx[i]
            ny = y + my[i]
            
            if 0 <= nx < h and 0 <= ny < w and MAP[nx][ny] == 1:
                MAP[nx][ny] = 2
                q.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
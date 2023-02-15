N, M = map(int, input().split())

A, B = [], []
for _ in range(N):
    am = list(map(int, input().split()))
    A.append(am)
    
for _ in range(N):
    bm = list(map(int, input().split()))
    B.append(bm)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
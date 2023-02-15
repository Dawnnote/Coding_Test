K, N = map(int, input().split())
cm = [int(input()) for _ in range(K)]

pl, pr = 1, max(cm)

while pl <= pr:
    pc = (pl + pr) // 2
    line = 0
    for i in cm:
        line += i // pc
    
    if line >= N:
        pl = pc + 1
    else:
        pr = pc - 1
        
print(pr)
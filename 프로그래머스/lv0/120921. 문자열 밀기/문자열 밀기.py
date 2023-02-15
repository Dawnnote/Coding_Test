def solution(A, B):
    result = -1
    cnt = 0
    ch = ''
    
    for _ in range(len(A)):
        ch = A[-1]
        A = ch + A[:-1]
        cnt += 1
        if A == B:
            result = cnt
            if cnt == len(A):
                result = 0
            
    return result
    
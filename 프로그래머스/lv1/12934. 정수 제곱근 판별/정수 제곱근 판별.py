def solution(n):
    N = n**0.5
    if N%1==0:
        return (N+1)**2
    
    return -1
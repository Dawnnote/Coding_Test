def solution(s):
    s = sorted(s)
    lis = []
    
    for i in s:
        if s.count(i) == 1:
            lis.append(i)
    
    return ''.join(lis)
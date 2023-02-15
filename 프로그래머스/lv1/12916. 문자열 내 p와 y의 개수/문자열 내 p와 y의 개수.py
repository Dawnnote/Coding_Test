def solution(s):
    s = s.lower()
    p_cnt = 0
    y_cnt = 0
    
    for i in s:
        if i == 'p':
            p_cnt += 1
        if i == 'y':
            y_cnt += 1
            
    if p_cnt == y_cnt:
        return True
    return False

    
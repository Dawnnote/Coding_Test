def solution(emergency):
    result = []
    dic = {}
    
    sort_em = sorted(emergency, reverse = True)
    
    for idx in range(len(sort_em)):
        dic[sort_em[idx]] = idx+1
    
    for i in emergency:
        result.append(dic[i])
    
    return result
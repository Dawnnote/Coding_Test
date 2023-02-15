def solution(spell, dic):
    dic = list(set(dic))
    result = 2
    
    for i in range(len(dic)):
        count = 0
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                count += 1
                if count == len(spell):
                    result = 1
    
    return result
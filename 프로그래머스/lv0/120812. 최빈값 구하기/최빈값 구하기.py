def solution(array):
    s = set(array)
    dic = {}
    result = 0
    cnt = 0
    
    for i in s:
        dic[i] = array.count(i)

    for k, v in dic.items():
        if v == max(dic.values()):
            result = k
            cnt += 1

            if cnt > 1:
                result = -1

    return result
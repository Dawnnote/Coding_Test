def solution(numlist, n):

    numlist = sorted(numlist, reverse = True)
    dic = {}
    result = []

    for i in numlist:
        dic[i] = abs(i - n)


    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse = False))

    for k, v in dic.items():
        result.append(k)

    return result
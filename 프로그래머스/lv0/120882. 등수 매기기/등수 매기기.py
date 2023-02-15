def solution(score):
    lis = []
    result = []
    for i in range(len(score)):
        lis.append(sum(score[i])/len(score[i]))

    sort_lis = sorted(lis, reverse = True)

    for i in lis:
        result.append(sort_lis.index(i)+1)

    return result
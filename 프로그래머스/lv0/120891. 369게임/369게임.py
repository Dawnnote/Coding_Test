def solution(order):
    answer = [3, 6, 9]
    lis_od = list(str(order))
    result = 0
    
    for i in range(len(lis_od)):
        for k in range(3):
            if int(lis_od[i]) == answer[k]:
                result += 1
    return result
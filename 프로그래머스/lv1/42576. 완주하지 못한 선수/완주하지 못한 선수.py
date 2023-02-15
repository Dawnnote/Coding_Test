def solution(participant, completion):
    part_dic = {i:0 for i in participant}

    for name in participant:
        part_dic[name] += 1

    for name in completion:
        part_dic[name] -= 1

    for k, v in part_dic.items():
        if v == 1:
            result = k
            
    return result
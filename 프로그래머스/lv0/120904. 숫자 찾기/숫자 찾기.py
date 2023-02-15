def solution(num, k):
    s_num = str(num)
    for i in range(len(s_num)):
        if int(s_num[i]) == k:
            return i+1
    return -1
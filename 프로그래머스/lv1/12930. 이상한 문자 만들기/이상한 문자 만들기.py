def solution(s):

    result = ''
    cnt = 0
    for i in s:

        if i == ' ':
            cnt = -1

        if cnt%2==0:
            result += i.upper()
        else:
            result += i.lower()
        cnt += 1
    
    return result
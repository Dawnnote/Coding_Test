def divisor(n, limit, power):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            div.append(n//i)
            div.append(i)
    if len(set(div)) > limit:
        return power
    return len(set(div))

def solution(number, limit, power):
    result = 0
    for i in range(1, number+1):
        num = divisor(i, limit, power)
        result += num
        
    return result


# 두번째 코드 (성공)
# def divisor(n):
#     cnt = 0
#     for j in range(1, int(n**0.5)+1):
#         if n%j == 0:
#             if n//j == j:
#                 cnt += 1
#             else:
#                 cnt += 2
        
#     if cnt > limit:
#         return power
#     return cnt
        
# def solution(number, limit, power):
#     answer = 0
#     for i in range(1, number+1):
#         num = divisor(i, limit, power)
#         answer += num
#     return answer

# 첫번째 코드 (시간초과 실패)
#     lis = list(range(1,number+1))

#     result = []
#     for i in lis:
#         cnt = 0
#         for j in range(1, i+1):
#             if i%j == 0:
#                 cnt += 1

#         result.append(cnt)

#     for i in range(len(result)):
#         if limit < result[i]:
#             result[i] = power

#     return sum(result)
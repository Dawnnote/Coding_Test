def solution(i, j, k):
    # count() 함수를 쓰면 쉽게 할 수 있음
    cnt = 0
    lis = []
    
    # 숫자가 두자리 이상인 경우도 각각 한자리씩 나타낼 수 있도록 함
    for num_1 in range(i, j+1):
        if len(str(num_1)) >= 2:
            lis.extend(sorted(str(num_1)))
        elif str(k) in str(num_1):
            cnt += 1
    
    # 두자리 이상 숫자 비교
    for num_2 in range(len(lis)):
        if str(k) in lis[num_2]:
            cnt += 1
    
    return cnt
def solution(board, moves):
    dic = {}
    dic_key = 1 # 딕셔너리 키값

    # 보드의 열별로 딕셔너리 키(행번호)와 값 저장
    for i in range(len(board)):
        lis = [] # lis 초기화
        for j in board:
            if j[i] == 0:           # 0은 제외하고 넣기 위함
                continue
            lis.append(j[i])
        dic[dic_key] = lis
        dic_key += 1

    # [[0, 0, 0, 0, 0],
    #  [0, 0, 1, 0, 3],
    #  [0, 2, 5, 0, 1],
    #  [4, 2, 4, 4, 2],
    #  [3, 5, 1, 3, 1]]


    #   1  2  3  4  5     <- key 값
    #   :  :  :  :  :
    # [[3, 2, 1, 4, 3],   <- value 값들
    #  [4, 2, 5, 3, 1],
    #  [   5, 4, 0, 2],
    #  [      1     1]],


    # 바구니에 담아주기
    basket = []
    for i in moves:
        for k, v in dic.items():
            if i == k:              # moves 와 보드 열(키값)이 같다면
                if dic[k] == []:    # 보드(열) 안에 값이 '[]' 비어있으면 다음 실행문으로 패스
                    pass
                else:
                    basket.append(dic[k][0])
                    dic[k].pop(0)   # 바구니에 담아준 인형은 보드에서 삭제


    # 2개가 겹쳐서 사라진 인형의 수
    result = []
    doll = 0 # 사라진 인형의 수
    for i in range(len(basket)):        # result = [] -> result[-1] error
        if result[-1:] == [basket[i]]:  # 들어있는 (마지막) 인형과, 이제 넣을 인형이 같다면
            result.pop(-1)              # 들어있는 마지막 인형 삭제
            doll += 2                   # 인형이 겹치면 2개는 무조건 사라지므로 +2
            continue                    # 겹치는 새로운 인형을 넣을 필요가 없기 때문에 continue
        result.append(basket[i])

    return doll
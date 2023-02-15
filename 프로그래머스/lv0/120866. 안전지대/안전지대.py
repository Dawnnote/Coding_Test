def solution(board):
    x = [0, 0, 1, -1, 1, -1, -1, 1]
    y = [1, -1, 0, 0, -1, 1, -1, 1]
    lis = []
    result = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                lis.append([i, j])

    for lis_x, lis_y in lis:
        for i in range(8):
            nx = x[i] + lis_x
            ny = y[i] + lis_y
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                pass
            else:
                board[nx][ny] = 1


    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                result += 1
                
    return result
import numpy as np

def solution(keyinput, board):
    key = {'up':[0,1], 'down': [0,-1], 'left':[-1,0], 'right':[1,0]}
    result = np.array([0, 0])
    
    for i in range(len(keyinput)):
        for k, v in key.items():
            if keyinput[i] == k:
                result = np.add(result, key[k])
    
                if abs(result[0]) > board[0]//2:
                    if result[0] < -(board[0]//2):
                        result[0] += (abs(result[0]) - board[0]//2)
                    else:
                        result[0] -= (abs(result[0]) - board[0]//2)

                elif abs(result[1]) > board[1]//2:
                    if result[1] < -(board[1]//2):
                        result[1] += (abs(result[1]) - board[1]//2)
                    else:
                        result[1] -= (abs(result[1]) - board[1]//2)

    return result.tolist()
    
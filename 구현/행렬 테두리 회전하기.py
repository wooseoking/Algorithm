import copy


def solution(rows, columns, queries):

    answer = []
    board = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = i*columns+j+1

    for y1,x1,y2,x2 in queries:
        board ,minval = rotate(board,y1-1,x1-1,y2-1,x2-1)
        answer.append(minval)
    return answer

def rotate(board,y1,x1,y2,x2):
    tmp = []
    newboard = board

    for j in range(x1,x2):
        tmp.append(board[y1][j])
    for i in range(y1,y2):
        tmp.append(board[i][x2])
    for j in range(x2,x1,-1):
        tmp.append(board[y2][j])
    for i in range(y2,y1,-1):
        tmp.append(board[i][x1])
    tmp = tmp[-1:] + tmp[:-1]
    minval = min(tmp)
    idx = 0
    for j in range(x1,x2):
        newboard[y1][j] = tmp[idx]
        idx+=1
    for i in range(y1,y2):
        newboard[i][x2] = tmp[idx]
        idx+=1
    for j in range(x2,x1,-1):
        newboard[y2][j] = tmp[idx]
        idx+=1
    for i in range(y2,y1,-1):
        newboard[i][x1] = tmp[idx]
        idx+=1

    return newboard,minval
def rotate(a,y1,x1,y2,x2):
    tmp = []
    for j in range(x1,x2):
        tmp.append(a[y1][j])
    for i in range(y1,y2):
        tmp.append(a[i][x2])
    for j in range(x2,x1,-1):
        tmp.append(a[y2][j])
    for i in range(y2,y1,-1):
        tmp.append(a[i][x1])

    idx = 0
    tmp = tmp[-1:] + tmp[:-1]
    min_n = min(tmp)
    for j in range(x1,x2):
        a[y1][j] = tmp[idx]
        idx+=1

    for i in range(y1,y2):
        a[i][x2] = tmp[idx]
        idx += 1

    for j in range(x2,x1,-1):
        a[y2][j] = tmp[idx]
        idx += 1

    for i in range(y2,y1,-1):
        a[i][x1] = tmp[idx]
        idx += 1

    return min_n

def solution(rows, columns, queries):
    answer = []
    board = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    for y1,x1,y2,x2 in queries:
        min_num = rotate(board,y1-1,x1-1,y2-1,x2-1)
        answer.append(min_num)

    return answer
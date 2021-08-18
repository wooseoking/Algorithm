n = int(input())
col = 2*n-1
row = n
idx = n-1
board = [[0]*col for _ in range(row)]
for i in range(col):
    cnt = 2*i + 1
    for j in range(idx,idx+cnt):
        board[i][j] = 1
    idx-=1
    if idx<0:break
for i in range(row):
    Blank = False
    for j in range(col):
        if board[i][j]==0 and not Blank:print(' ',end='')
        elif board[i][j] == 1:
            Blank = True
            print('*',end='')
        elif board[i][j]==0 and Blank:
            print()
            break

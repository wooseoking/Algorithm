n = int(input())
board = [[' ']*(2*n) for _ in range(2*n - 1)]
for i in range(2*n-1):
    if i <= (2*n -1) //2:
        for j in range(2*n):
            if j<=i or i+j>=2*n-1:
                board[i][j] = '*'
    else:
        for j in range(2*n):
            if j>i or i+j < 2*n-1:
                board[i][j] = '*'
for i in range(2*n-1):
    for j in range(2*n):
        print(board[i][j],end='')
    print()
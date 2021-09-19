n = int(input())
board = [[' ']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i-j==0 or n-i-j-1==0:
            board[i][j]='*'
for i in range(n):
    for j in range(n):
        print(board[i][j],end='')
    print()
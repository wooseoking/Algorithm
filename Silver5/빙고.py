def checkBingo(erase):
    set_ = 0
    #가로 체크
    for i in range(N):
        if sum(erase[i]) == N :set_+=1
    #세로체크
    for j in range(N):
        tmp = 0
        for i in range(N):
            tmp+=erase[i][j]
        if tmp==N:set_+=1
    #대각체크
    tmp1 = 0
    for i in range(N):
        tmp1+=erase[i][i]
    if tmp1==N:set_+=1
    #역대각 체크
    tmp2 = 0
    for i in range(N):
        tmp2+=erase[i][N-1-i]
    if tmp2 == N :set_+=1
    return set_>=3

N = 5
Location = [None]*26
Board =[[0]*N for _ in range(N)]
Erase = [[0]*N for _ in range(N)]
for i in range(N):
    Board[i] = list(map(int,input().split()))
for i in range(N):
    for j in range(N):
        num = Board[i][j]
        Location[num] = (i,j)
Order = [[0]*N for _ in range(N)]
for i in range(N):
    Order[i] = list(map(int,input().split()))

cnt = 0

for i in range(N):
    for j in range(N):

        if checkBingo(Erase):
            print(cnt)
            exit(0)
        num = Order[i][j]
        y,x = Location[num]
        Erase[y][x] = 1
        cnt+=1
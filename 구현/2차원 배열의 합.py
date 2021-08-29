n,m = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
k = int(input())
for _ in range(k):
    a,b,c,d = map(int,input().split())
    a-=1
    b-=1
    c-=1
    d-=1
    answer = 0
    for i in range(a,c+1):
        for j in range(b,d+1):
            answer+=board[i][j]
    print(answer)
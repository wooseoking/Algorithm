N,M =map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j]%=1000

def POW(a,n):
    if n==1:return a
    y = POW(a,n//2)

    RESULT = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                RESULT[i][j] += y[i][k] * y[k][j]
                RESULT[i][j]%=1000

    if n%2==0: return RESULT
    else:
        NEW_RESULT = [[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    NEW_RESULT[i][j] += RESULT[i][k] * A[k][j]
                    NEW_RESULT[i][j]%=1000


        return NEW_RESULT

ans = POW(A,M)
for rows in ans:
    print(*rows,sep=' ')
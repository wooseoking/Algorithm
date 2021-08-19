dz = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dx = [-1,1,0,0,0,0]

while True:
    L,R,C = map(int,input().split())
    if L==0 and R==0 and C==0:break
    board = [[[]*C for _ in range(R)]for _ in range(L)]
    d = [[[-1]*C for _ in range(R)]for _ in range(L)]
    for i in range(L):
        board[i] = [list(map(str,input().strip()))for _ in range(R)]
        input()
    sz,sy,sx,ez,ey,ex = -1,-1,-1,-1,-1,-1
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k]=='S':
                    sz,sy,sx = i,j,k
                if board[i][j][k]=='E':
                    ez,ey,ex = i,j,k
    q = [(sz,sy,sx)]
    d[sz][sy][sx] = 0
    ans = -1
    while q:
        nz,ny,nx = q.pop(0)
        if nz==ez and ny==ey and nx == ex:
            ans = d[nz][ny][nx]
            break
        for k in range(6):
            nextz,nexty,nextx = nz+dz[k],ny+dy[k],nx+dx[k]
            if not (0<=nextz<L and 0<=nexty<R and 0<=nextx<C):continue
            if board[nextz][nexty][nextx]=='#':continue
            if d[nextz][nexty][nextx]!=-1:continue
            d[nextz][nexty][nextx] = d[nz][ny][nx]+1
            q.append((nextz,nexty,nextx))
    if ans!=-1:print("Escaped in",ans,"minute(s).")
    else:print("Trapped!")

import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x,n,m):
    return 0<=y<n and 0<=x<m

def solution(maze):
    answer = 0
    WALL = 5
    MAXN = 4
    #초기화
    n,m = len(maze),len(maze[0])
    sry,srx,ery,erx,sby,sbx,eby,ebx = 0,0,0,0,0,0,0,0
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == WALL:continue
            
            if maze[i][j] == 1:
                sry,srx = i,j
            elif maze[i][j] == 2:
                sby,sbx = i,j
            elif maze[i][j] == 3:
                ery,erx = i,j
            elif maze[i][j] == 4:
                eby,ebx = i,j
            maze[i][j] = 0
            
    
    
    #bfs
    rv = [[False]*m for _ in range(n)]
    bv = [[False]*m for _ in range(n)]
    rv[sry][srx] = True
    bv[sby][sbx] = True
    q = []
    q.append([sry,srx,sby,sbx,0,rv,bv])
    
    while q:
        ry,rx,by,bx,cnt,rv,bv = q.pop(0)
        print('depth : ',cnt, ' --> ',ry,rx,by,bx)
        #성공조건
        if ry == ery and rx == erx and by == eby and bx == ebx: return cnt
        
        #빨강 끝났다면 처리
        if ry == ery and rx == erx:
            
            for k in range(4):
                nry,nrx,nby,nbx = ry,rx,by,bx
                nrv,nbv = copy.deepcopy(rv),copy.deepcopy(bv)
                
                nby,nbx = by + dy[k] , bx + dx[k]
                
                if (not inside(nry,nrx,n,m)) or (not inside(nby,nbx,n,m)):continue
                if ry == nby and rx == nbx and nry == by and nrx == bx:continue
                if nbv[nby][nbx]:continue               
                if maze[nry][nrx] == WALL or maze[nby][nbx] == WALL:continue
                
                if nry == nby and nrx == nbx:continue
                nrv[nry][nrx] = True
                nbv[nby][nbx] = True
                
                q.append([nry,nrx,nby,nbx,cnt + 1,nrv,nbv])
        #파랑 끝났다면
        elif by == eby and bx == ebx: 
            for k in range(4):
                nry,nrx,nby,nbx = ry,rx,by,bx
                nrv,nbv = copy.deepcopy(rv),copy.deepcopy(bv)
                
                nry,nrx = ry + dy[k] , rx + dx[k]
                if (not inside(nry,nrx,n,m)) or (not inside(nby,nbx,n,m)):continue
                if ry == nby and rx == nbx and nry == by and nrx == bx:continue
                if nrv[nry][nrx]:continue
                if maze[nry][nrx] == WALL or maze[nby][nbx] == WALL:continue
                if nry == nby and nrx == nbx:continue
                nrv[nry][nrx] = True
                nbv[nby][nbx] = True
                q.append([nry,nrx,nby,nbx,cnt + 1,nrv,nbv])

        #둘다 안끝남
        else:
            for rk in range(4):
                for bk in range(4):
                    nry,nrx,nby,nbx = ry,rx,by,bx
                    nrv,nbv = copy.deepcopy(rv),copy.deepcopy(bv)
                    
                    nry,nrx = ry + dy[rk] , rx + dx[rk]
                    nby,nbx = by + dy[bk] , bx + dx[bk]
                    if (not inside(nry,nrx,n,m)) or (not inside(nby,nbx,n,m)):continue
                    if ry == nby and rx == nbx and nry == by and nrx == bx:continue
                    if nrv[nry][nrx]:continue
                    if nbv[nby][nbx]:continue
                    if maze[nry][nrx] == WALL or maze[nby][nbx] == WALL:continue
                    if nry == nby and nrx == nbx:continue
                    nrv[nry][nrx] = True
                    nbv[nby][nbx] = True
                    q.append([nry,nrx,nby,nbx,cnt + 1,nrv,nbv])

                
    return 0
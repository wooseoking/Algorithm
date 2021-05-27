n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def inside(y,x):
    return 0<=y<n and 0<=x<m

def getGaro():
    ret = 0
    for y in range(n):
        for x in range(m):
            ok1 = True
            ok2 = True
            s1 = 0
            s2 = 0
            for k in range(4):
                if not inside(y+k,x):
                    ok1 = False
                    continue
                s1 +=a[y+k][x]
            for k in range(4):
                if not inside(y,x+k):
                    ok2 = False
                    continue
                s2 +=a[y][x+k]
            if ok1:ret = max(ret,s1)
            if ok2:ret = max(ret,s2)
    return ret

def Nemo():
    ret = 0
    dy = [0,1,1,0]
    dx = [0,0,1,1]
    for y in range(n):
        for x in range(m):
            ok1 = True
            s1 = 0
            for k in range(4):
                ny = y+dy[k]
                nx = x+dx[k]
                if not inside(ny,nx):
                    ok1 = False
                    continue
                s1+=a[ny][nx]
            if ok1:
                ret = max(ret,s1)
    return ret

def Orange():
    ans = 0
    #type1
    dy1=[0,1,2,2,1,0]
    dx1=[0,0,0,1,1,1]

    #type2
    dy2 = [0,0,0,1,1,1]
    dx2 = [0,1,2,2,1,0]
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y+dy1[k]
                nx = x+dx1[k]
                if not inside(ny,nx):
                    ok = False
                    continue
                s+=a[ny][nx]

            if ok:
                temp1 = a[y][x+1] + a[y+1][x+1]
                temp2 = a[y][x] + a[y+1][x]
                temp3 = a[y+1][x] + a[y+2][x]
                temp4 = a[y+1][x+1] + a[y+2][x+1]

                ret = max(s-temp1,s-temp2,s-temp3,s-temp4)
                ans = max(ret,ans)
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y + dy2[k]
                nx = x + dx2[k]
                if not inside(ny, nx):
                    ok = False
                    continue
                s += a[ny][nx]

            if ok:
                temp1 = a[y][x] + a[y][x+1]
                temp2 = a[y][x+1] + a[y][x+2]
                temp3 = a[y+1][x] + a[y + 1][x + 1]
                temp4 = a[y + 1][x + 1] + a[y + 1][x + 2]
                ret = max(s - temp1, s - temp2, s - temp3, s - temp4)
                ans = max(ret,ans)
    return ans

def Green():
    ans = 0
    # type1
    dy1 = [0, 1, 2, 2, 1, 0]
    dx1 = [0, 0, 0, 1, 1, 1]

    # type2
    dy2 = [0, 0, 0, 1, 1, 1]
    dx2 = [0, 1, 2, 2, 1, 0]
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y + dy1[k]
                nx = x + dx1[k]
                if not inside(ny, nx):
                    ok = False
                    continue
                s += a[ny][nx]

            if ok:
                temp1 = a[y][x] + a[y+2][x+1]
                temp2 = a[y][x+1] + a[y+2][x]
                ret = max(s - temp1, s - temp2)
                ans = max(ret, ans)
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y + dy2[k]
                nx = x + dx2[k]
                if not inside(ny, nx):
                    ok = False
                    continue
                s += a[ny][nx]

            if ok:
                temp1 = a[y][x+2] + a[y+1][x]
                temp2 = a[y][x] + a[y+1][x + 2]

                ret = max(s - temp1, s - temp2)
                ans = max(ret, ans)
    return ans

def Purple():
    ans = 0
    # type1
    dy1 = [0, 1, 2, 2, 1, 0]
    dx1 = [0, 0, 0, 1, 1, 1]

    # type2
    dy2 = [0, 0, 0, 1, 1, 1]
    dx2 = [0, 1, 2, 2, 1, 0]
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y + dy1[k]
                nx = x + dx1[k]
                if not inside(ny, nx):
                    ok = False
                    continue
                s += a[ny][nx]

            if ok:
                temp1 = a[y][x+1] + a[y + 2][x + 1]
                temp2 = a[y][x] + a[y + 2][x]
                ret = max(s - temp1, s - temp2)
                ans = max(ret, ans)
    for y in range(n):
        for x in range(m):
            ok = True
            s = 0
            for k in range(6):
                ny = y + dy2[k]
                nx = x + dx2[k]
                if not inside(ny, nx):
                    ok = False
                    continue
                s += a[ny][nx]

            if ok:
                temp1 = a[y][x] + a[y][x+2]
                temp2 = a[y+1][x] + a[y + 1][x + 2]

                ret = max(s - temp1, s - temp2)
                ans = max(ret, ans)
    return ans

print(max(getGaro(),Nemo(),Orange(),Purple(),Green()))
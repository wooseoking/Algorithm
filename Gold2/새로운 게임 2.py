def inside(y,x):
    return 0<=y<n and 0<=x<n

def solve(color,a,horses):
    t = 0
    while 1:
        if t>=1000:
            return -1
        t+=1
        for i in range(k):
            y,x,d = horses[i]
            ny = y + dy[d]
            nx = x + dx[d]
            if not inside(ny,nx) or color[ny][nx]==2:
                nd = rev_d[d]
                ny,nx = y+dy[nd],x+dx[nd]
                horses[i][2] = nd
                if not inside(ny,nx) or color[ny][nx]==2:
                    horses[i][2] = nd
                    continue
            if color[ny][nx]==0:
                idx = a[y][x].index(i)
                temp = a[y][x][idx:]
                a[ny][nx] +=temp
                for num in temp:
                    horses[num] = [ny,nx,horses[num][2]]
                del a[y][x][idx:]
                if len(a[ny][nx])>=4:return t
                continue
            if color[ny][nx]==1:
                idx = a[y][x].index(i)
                temp = a[y][x][idx:][::-1]

                a[ny][nx] += temp
                for num in temp:
                    horses[num] = [ny,nx,horses[num][2]]
                del a[y][x][idx:]
                if len(a[ny][nx]) >= 4: return t
                continue

if __name__ == '__main__':

    n, k = map(int, input().split())
    color = [list(map(int, input().split())) for _ in range(n)]
    horses = []
    a = [[[] * n for _ in range(n)] for _ in range(n)]

    for i in range(k):
        y, x, d = map(int, input().split())
        a[y - 1][x - 1].append(i)
        horses.append([y - 1, x - 1, d - 1])

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    rev_d = {0: 1, 1: 0, 2: 3, 3: 2}

ans = solve(color,a,horses)
print(ans)
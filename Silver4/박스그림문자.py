n,m = map(int,input().split())
a = [list(input()) for _ in range(3*n)]
#    위 아래 왼 오
cy = [-2,2,0,0]
cx = [0,0,-2,2]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y_,x_):
    return 0<=y_<3*n and 0<=x_<3*m

for i in range(n):
    for j in range(m):
        if (i+j)%2==0:continue
        y,x = 3*i+1,3*j+1
        for k in range(4):
            ny,nx = y + cy[k],x+cx[k]
            if inside(ny,nx) and a[ny][nx] =='#':
                a[y+dy[k]][x+dx[k]] = '#'
                a[y][x] = '#'


for i in range(3*n):
    for j in range(3*m):
        print(a[i][j],end='')
    print()
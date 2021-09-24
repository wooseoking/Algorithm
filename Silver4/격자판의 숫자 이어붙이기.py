dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<4 and 0<=x<4

def go(r,c,cnt):
    if cnt ==7:
        num = ''.join(map(str,result))
        table.add(num)
        return

    result.append(a[r][c])
    for k in range(4):
        ny,nx = r+dy[k],c+dx[k]
        if not inside(ny,nx):continue
        go(ny,nx,cnt+1)
    result.pop(-1)

t = int(input())

for iter in range(t):
    table = set()
    a = [list(map(int,input().split())) for _ in range(4)]
    for y in range(4):
        for x in range(4):
            result = []
            go(y,x,0)
    print('#',iter+1,len(table))
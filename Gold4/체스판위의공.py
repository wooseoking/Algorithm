dy = [-1,-1,-1,0,1,1,1,0]
dx = [-1,0,1,1,1,0,-1,-1]

def inside(y,x):
    return 0<=y<r and 0<=x<c

def Parent(x):
    if parent[x]==x:return x
    parent[x] = Parent(parent[x])
    return parent[x]

if __name__ == "__main__":
    r,c = map(int,input().split())
    a = [list(map(int,input().split()))for _ in range(r)]
    ans = [[0]*c for _ in range(r)]
    parent = [0]*r*c
    for i in range(r):
        for j in range(c):
            y = i
            x = j
            for k in range(8):
                ny = i+dy[k]
                nx = j+dx[k]
                if inside(ny,nx) and a[ny][nx]<a[y][x]:
                    y = ny
                    x = nx
            parent[i*c+j] = y*c+x
    for i in range(r*c):
        Parent(i)
    for v in parent:
        y,x = v//c,v%c
        ans[y][x]+=1
    for i in range(r):
        for v in ans[i]:
            print(v,end=' ')
        print()
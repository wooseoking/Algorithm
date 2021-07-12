dy = [-1,1,0,0]
dx = [0,0,-1,1]
def inside(row,col):
    return 1<=row<=n and 0<=col<m

def rotate(a_,d_,k_):
    if d_==0:
        tmp = a_[-k_:]+a_[:-k_]
    else:
        tmp = a_[k_:]+a_[:k_]
    return tmp

def check_list():
    global a
    #1번
    e = []
    for i in range(1,n+1):
        if a[i][0]==-1 or a[i][m-1]==-1:continue
        if a[i][0]==a[i][m-1]:
            e.append((i,0))
            e.append((i,m-1))
    for i in range(1,n+1):
        for j in range(m):
            for k_ in range(4):
                if a[i][j]==-1:continue
                ny,nx = i+dy[k_],j+dx[k_]
                if inside(ny,nx) and a[i][j]==a[ny][nx]:
                    e.append((i,j))
    return e

def go():
    global a
    mean = 0
    cnt = 0
    for i in range(1,n+1):
        for j in range(m):
            if a[i][j]==-1:continue
            cnt+=1
            mean+=a[i][j]
    if cnt==0:mean=0
    else:mean /= cnt

    for i in range(1,n+1):
        for j in range(m):
            if a[i][j]==-1:continue
            if a[i][j]>mean:
                a[i][j]-=1
            elif a[i][j]<mean:
                a[i][j]+=1

def getAns():
    ans = 0
    for i in range(1,n+1):
        for j in range(m):
            if a[i][j]==-1:continue
            ans+=a[i][j]
    return ans
n,m,t = map(int,input().split())
a = [[]for _ in range(n+1)]
for i in range(1,n+1):
    a[i] = list(map(int,input().split()))

for _ in range(t):
    x,d,k = map(int,input().split())

    for i in range(1,n+1):
        if i%x==0:
            a[i] = rotate(a[i],d,k)

    erase = check_list()

    for i,j in erase:
        a[i][j] = -1

    if not erase:go()
ans = getAns()
print(ans)
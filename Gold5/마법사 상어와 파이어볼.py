dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
odd_even = [0,2,4,6]
not_odd_even = [1,3,5,7]

def even(d):
    ok = True
    for v in d:
        if v%2==1:ok=False
    return ok

def odd(d):
    ok = True
    for v in d:
        if v%2==0:ok = False
    return ok


def newlocation(row,col,si,di):
    ny,nx = row,col
    ny+=dy[di]*si
    nx+=dx[di]*si
    ny%=n
    nx%=n
    return ny,nx

def move():
    global a
    newa = [[[]*n for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(len(a[i][j])):
                m,s,d = a[i][j][k]
                ny ,nx = newlocation(i,j,s,d)
                newa[ny][nx].append((m,s,d))
    a = newa


def second():
    global a

    for i in range(n):
        for j in range(n):
            if len(a[i][j])>=2:
                M = 0
                S = 0
                dir = []
                for m,s,d in a[i][j]:
                    M+=m
                    S+=s
                    dir.append(d)

                M//=5
                S//=len(a[i][j])
                a[i][j].clear()
                if M==0:continue
                if even(dir) or odd(dir):#even or odd
                    for k in range(4):
                        a[i][j].append((M,S,odd_even[k]))
                else:
                    for k in range(4):
                        a[i][j].append((M,S,not_odd_even[k]))


def getMass():
    global a
    MASS = 0
    for i in range(n):
        for j in range(n):
            for k in range(len(a[i][j])):
                MASS +=a[i][j][k][0]
    return MASS
if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = [[[]*n for _ in range(n)]for _ in range(n)]
    for i in range(m):
        r,c,mass,s,d = map(int,input().split())
        a[r-1][c-1].append((mass,s,d))
    ans = 0
    for _ in range(k):
        move()
        second()
    print(getMass())
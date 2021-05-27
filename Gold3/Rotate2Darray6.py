def First(a,l):
    n = len(a)
    k = pow(2,l)
    b = [[0]*n for _ in range(n)]

    if l ==0 :return a

    for i in range(0,n,k):
        for j in range(0,n,k):
           for u in range(k):
               for v in range(k):
                   b[i+u][j+v] = a[i-u+k-1][j+v]
    a = b
    return a

def Second(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a

    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[i + u ][j - v + k -1]
    a = b
    return a

def Third(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[i + v ][j -u+k-1]
    a = b
    return a
def Four(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[i -v+k-1 ][j +u]
    a = b
    return a
def Five(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[n-k-i+u][j+v]
    a = b
    return a

def Six(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0,n,k):
        for j in range(0,n,k):
            for u in range(k):
                for v in range(k):
                    b[i+u][j+v] = a[i+u][v-j+n-k]
    a = b
    return a

def Seven(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[u + n-j-k][i+v]
    a = b
    return a

def Eight(a,l):
    n = len(a)
    k = pow(2, l)
    b = [[0] * n for _ in range(n)]

    if l == 0: return a
    for i in range(0, n, k):
        for j in range(0, n, k):
            for u in range(k):
                for v in range(k):
                    b[i + u][j + v] = a[j + u][v + n-i-k]
    a = b
    return a
N,R = map(int,input().split())
N = pow(2,N)
Rotation = []
ans = [list(map(int,input().split())) for _ in range(N)]
for _ in range(R):
    x,y = map(int,input().split())
    Rotation.append((x,y))

for k_, l_ in Rotation:
    if k_ ==1:
        ans = First(ans,l_)
    elif k_==2:
        ans = Second(ans, l_)
    elif k_ == 3:
        ans = Third(ans, l_)
    elif k_ == 4:
        ans = Four(ans, l_)
    elif k_ == 5:
        ans = Five(ans, l_)
    elif k_ == 6:
        ans = Six(ans, l_)
    elif k_ == 7:
        ans = Seven(ans, l_)
    elif k_ == 8:
        ans = Eight(ans, l_)
print(ans)
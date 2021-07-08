import copy

n,m,R = map(int,input().split())
a = [list(map(int,input().split()))for _ in range(n)]
query = list(map(int,input().split()))

def go1():
    global a
    r,c = len(a),len(a[0])
    na = copy.deepcopy(a)
    for i in range(r):
        for j in range(c):
            na[i][j] = a[r-i-1][j]
    return na
def go2():
    global a
    r,c = len(a),len(a[0])
    na = copy.deepcopy(a)
    for i in range(r):
        for j in range(c):
            na[i][j] = a[i][c-j-1]
    return na
def go3():
    global a
    r,c = len(a),len(a[0])
    na = [[0]*r for _ in range(c)]

    for i in range(c):
        for j in range(r):
            na[i][j] = a[r-j-1][i]

    return na

def go4():
    global a
    r,c = len(a),len(a[0])
    na = [[0] * r for _ in range(c)]

    for i in range(c):
        for j in range(r):
            na[i][j] = a[j][c-i-1]

    return na

def go5():
    global a
    r, c = len(a), len(a[0])
    na = copy.deepcopy(a)

    for i in range(r//2):
        for j in range(c//2):
            na[i][j] = a[i+r//2][j]

    for i in range(r//2):
        for j in range(c//2):
            na[i][j+c//2] = a[i][j]

    for i in range(r//2):
        for j in range(c//2):
            na[i+r//2][j+c//2] = a[i][j+c//2]

    for i in range(r//2):
        for j in range(c//2):
            na[i+r//2][j] = a[i+r//2][j+c//2]
    return na


def go6():
    global a
    r, c = len(a), len(a[0])
    na = copy.deepcopy(a)

    for i in range(r // 2):
        for j in range(c // 2):
            na[i][j] = a[i][j+c//2]

    for i in range(r // 2):
        for j in range(c // 2):
            na[i+r//2][j] = a[i][j]

    for i in range(r // 2):
        for j in range(c // 2):
            na[i + r // 2][j + c // 2] = a[i+r//2][j]

    for i in range(r // 2):
        for j in range(c // 2):
            na[i][j+c//2] = a[i + r // 2][j + c // 2]
    return na

for what in query:
    if what==1:
        a = go1()
    elif what==2:
        a = go2()
    elif what==3:
        a = go3()
    elif what==4:
        a = go4()
    elif what==5:
        a = go5()
    elif what==6:
        a = go6()
for rows in a:
    print(*rows,sep=' ')
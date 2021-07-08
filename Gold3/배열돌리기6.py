import copy

n,R = map(int,input().split())
n = pow(2,n)
a = [list(map(int,input().split()))for _ in range(n)]
query = []
for _ in range(R):
    x,y = map(int,input().split())
    query.append((x,y))

def go1(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n // l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i * l
            sx = j * l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy + inner_i][sx + inner_j] = a[sy + l - inner_i - 1][sx + inner_j]
    a = na

def go2(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n // l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i * l
            sx = j * l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy + inner_i][sx + inner_j] = a[sy + inner_i][sx + l - inner_j -1]
    a = na

def go3(l):
    global a
    na = [[0]*n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[sy+l-inner_j-1][sx+inner_i]
    a = na

def go4(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[sy+inner_j][sx+l-inner_i-1]
    a = copy.deepcopy(na)

def go5(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            cy = (inner_cnt - i -1)*l
            cx = j*l

            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[cy+inner_i][cx+inner_j]
    a = copy.deepcopy(na)

def go6(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            cy = i*l
            cx = (inner_cnt - j -1)*l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[cy+inner_i][cx+inner_j]
    a = copy.deepcopy(na)

def go7(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            cy = (inner_cnt - j -1)*l
            cx = i*l
            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[cy+inner_i][cx+inner_j]
    a = copy.deepcopy(na)
def go8(l):
    global a
    na = [[0] * n for _ in range(n)]
    inner_cnt = n//l
    for i in range(inner_cnt):
        for j in range(inner_cnt):
            sy = i*l
            sx = j*l
            cy = j*l
            cx = (inner_cnt - i - 1)*l

            for inner_i in range(l):
                for inner_j in range(l):
                    na[sy+inner_i][sx+inner_j] = a[cy+inner_i][cx+inner_j]
    a = copy.deepcopy(na)
for k,L in query:
    if k == 1:
        go1(pow(2,L))
    if k == 2:
        go2(pow(2,L))
    if k == 3:
        go3(pow(2,L))
    if k == 4:
        go4(pow(2,L))
    if k == 5:
        go5(pow(2,L))
    if k == 6:
        go6(pow(2,L))
    if k == 7:
        go7(pow(2,L))
    if k == 8:
        go8(pow(2,L))
for rows in a:
    print(*rows,sep=' ')
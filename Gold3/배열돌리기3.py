def First(arr):
    r = len(arr)
    c = len(arr[0])
    b = [[0] * c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            b[i][j] = arr[r - i - 1][j]
    b = arr
    return arr

def Second(arr):
    r = len(arr)
    c = len(arr[0])
    b = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            b[i][j] = arr[i][c - j - 1]
    arr=b
    return arr

def Third(arr):
    n = len(arr)
    m = len(arr[0])
    b = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            b[i][j] = arr[n-j-1][i]
    arr = b
    return arr

def Four(arr):
    n = len(arr)
    m = len(arr[0])
    b = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = arr[j][m-i-1]
    arr = b
    return arr
def Five(arr):
    r = len(arr)
    c = len(arr[0])
    b = [[0] * c for _ in range(r)]
    for i in range(r // 2):
        for j in range(c // 2):
            b[i][j + c // 2] = arr[i][j]
            b[i + r // 2][j + c // 2] = arr[i][j + c // 2]
            b[i + r // 2][j] = arr[i + r // 2][j + c // 2]
            b[i][j] = arr[i + r // 2][j]
    arr = b
    return arr

def Six(arr):
    r = len(arr)
    c = len(arr[0])
    b = [[0] * c for _ in range(r)]
    for i in range(r // 2):
        for j in range(c // 2):
            b[i][j] = arr[i][j + c // 2]
            b[i ][j + c // 2] = arr[i + r // 2][j + c // 2]
            b[i + r // 2][j + c // 2] = arr[i + r // 2][j]
            b[i + r // 2][j] = arr[i][j]
    arr = b
    return arr

row, col, k= map(int, input().split())
ans = [list(map(int,input().split())) for _ in range(row)]
rotate = list(map(int,input().split()))


for op in rotate:
    if op==1:
        ans = First(ans)
    elif op==2:
        ans = Second(ans)
    elif op == 3:
        ans = Third(ans)
    elif op == 4:
        ans = Four(ans)
    elif op == 5:
        ans = Five(ans)
    elif op==6:
        ans = Six(ans)

for row in ans:
    print(*row,sep=' ')
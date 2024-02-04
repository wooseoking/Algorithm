t = int(input())

def rotate2DArray(array):
    n,m = len(array),len(array[0])
    newArray = [['']*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            newArray[i][j] = array[j][m-1-i]

    return newArray

def makePreProcessMap(array,maxK):
    n , m = len(array),len(array[0])
    newArray = [['.']*(m + 2*maxK + 2) for _ in range(n + 2*maxK + 2)]

    for i in range(maxK + 1,maxK + 1 + n):
        for j in range(maxK + 1,maxK+ 1 + m):
            newArray[i][j] = array[i - maxK - 1][j - maxK - 1]
    return newArray

def getCnt(array,k):
    res = set()
    cnt = 0
    n,m = len(array),len(array[0])
    #기본전략 = window Slicing
    for i in range(n - k - 1):
        for j in range(m - k - 1):
            # (i,j) 에서 두번째 그림으로 시작하는거임
            for c in range(k + 1):
                if array[i + c][j] == '#':
                    cnt -= 1
                if array[i + c][j + k + 1 - c] == '#':
                    cnt += 1

            res.add(cnt)

    return max(res)

for _ in range(t):
    n,m,k = map(int,input().split())
    a = [list(input()) for _ in range(n)]
    res = []

    for _ in range(4):
        a = rotate2DArray(a)
        preMap = makePreProcessMap(a,k)
        res.append(getCnt(preMap,k))
    print(max(res))

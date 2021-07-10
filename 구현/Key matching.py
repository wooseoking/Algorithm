import copy

def rotate(key):
    m = len(key)
    nk = copy.deepcopy(key)
    for i in range(m):
        for j in range(m):
            nk[i][j] = key[m-j-1][i]
    return nk

def check(Map,m,n):
    for i in range(m,m+n):
        for j in range(m,m+n):
            if Map[i][j]==0:return False
    return True

def Open(a,key,row,col):
    m = len(key)
    for i in range(row,row+m):
        for j in range(col,col+m):
            if a[i][j]!=key[i-row][j-col]:
                a[i][j]=1
            else:a[i][j]=0


def solution(key, lock):

    m = len(key)
    n = len(lock)
    a = [[0]*(2*m+n) for _ in range(2*m+n)]
    for i in range(m,m+n):
        for j in range(m,m+n):
            a[i][j] = lock[i-m][j-m]

    for i in range(1,m+n):
        for j in range(1,m+n):

            for _ in range(4):
                key = rotate(key)
                tmp_a = copy.deepcopy(a)
                #열어보고
                Open(tmp_a,key,i,j)
                if check(tmp_a,m,n):return True

    return False
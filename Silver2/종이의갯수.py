import sys
input = sys.stdin.readline
N = int(input())
a = list(list(map(int,input().split())) for _ in range(N))

minus=0
zero =0
one =0
def go(y,x,n):
    global minus,zero,one
    cur_num = a[y][x]
    ok = True

    for i in range(y,y+n):
        for j in range(x,x+n):
            if a[i][j]!=cur_num:
                ok = False
    if ok:
        if cur_num==-1:minus+=1
        if cur_num==0:zero+=1
        if cur_num==1:one+=1
        return

    for i in range(3):
        for j in range(3):
            go(y+i*n//3,x+j*n//3,n//3)

go(0,0,N)
print(minus,zero,one)
number = int("1325",base = 19)

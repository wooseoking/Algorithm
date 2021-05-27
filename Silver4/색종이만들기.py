import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

blue = 0
white = 0

def go(a,y,x,l):
    global blue
    global white
    ok = True
    ele = a[y][x]
    for i in range(y,y+l):
        for j in range(x,x+l):
            if a[i][j]!=ele:
                ok = False
    if ok:
        if ele==1:blue+=1
        elif ele==0:white+=1
        return
    ll = l//2
    go(a,y,x,ll)
    go(a,y+ll,x,ll)
    go(a,y+ll,x+ll,ll)
    go(a,y,x+ll,ll)
    return

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
go(a,0,0,n)
print(white)
print(blue)
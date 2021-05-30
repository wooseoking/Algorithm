import sys
sys.setrecursionlimit(100000000)
cnt = 0
ans = -1
def go(n,y,x,num):
    if n==2:
        for i in range(y,y+n):
            for j in range(x,x+n):
                if i==r and j ==c:
                    print(num)
                    exit(0)
                num+=1
        return
    t = n//2
    if y <= r < y + t and x <= c < x + t : go(t,y,x,num)
    if y <= r < y + t and x + t <= c < x + n : go(t,y,x+t,num+ pow(t,2))
    if y+t <= r < y + n and x <= c < x + t : go(t, y+t, x, num + 2*pow(t,2))
    if y+t <= r < y + n and x+t <= c < x + n : go(t, y+t, x+t, num + 3*pow(t,2))

N,r,c = map(int,input().split())
go(pow(2,N),0,0,0)
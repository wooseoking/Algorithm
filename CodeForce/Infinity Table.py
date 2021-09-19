def getN(num):
    n = 1
    while True:
        if n**2-2*n+2<=num<n**2+1:break
        n+=1
    return n,n**2-2*n+2

t = int(input())
for _ in range(t):
    target = int(input())
    col,start = getN(target)
    row = 1

    while True:
        if row==col or start==target:break
        row+=1
        start+=1

    if start==target:
        print(row,col)
        continue
    while True:
        if col==1 or start==target:break
        col-=1
        start+=1
    print(row,col)
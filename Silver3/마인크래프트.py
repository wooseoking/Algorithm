n,m,b = map(int,input().split())
a = [list(map(int,input().split()))for _ in range(n)]
result = []
for height in range(256+1):
    s = 0
    t = 0

    for i in range(n):
        for j in range(m):
           tmp = height - a[i][j]
           if tmp==0:continue
           elif tmp>0:
               t+=tmp
           else:
               t+=-2*tmp
           s+=tmp
    if s<=b:result.append((t,height))
result.sort(key=lambda l: (l[0],-l[1]))

print(result[0][0],result[0][1])
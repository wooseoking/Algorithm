import itertools

sx,sy = map(int,input().split())
ex,ey = map(int,input().split())
a = []
for k in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    a.append((x1,y1,x2,y2))
    a.append((x2,y2,x1,y1))

ans = abs(sx-ex) + abs(sy-ey)

for cnt in range(1,4):
    for x in itertools.permutations(a,cnt):
        tmp = 10*cnt
        tmp+= abs(x[0][0]-sx)+abs(x[0][1]-sy)
        interval = 0
        for prev,next in zip(x,x[1:]):
            interval += abs(prev[2]-next[0]) + abs(prev[3] - next[1])
        tmp+=abs(x[-1][2]-ex) + abs(x[-1][3]-ey)
        tmp+=interval
        ans =min(ans,tmp)

print(ans)
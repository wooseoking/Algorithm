import sys
input = sys.stdin.readline

N = int(input())
a = [[int(x) for x in input().split()] for _ in range(N)]
d = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]

d[0][1][2] = 1

for y in range(0,N):
    for x in range(1,N):
        for k in range(3):
            if k==0:
                if y-1<0:continue
                if a[y][x] ==0:
                    d[y][x][0] += d[y-1][x][0] + d[y-1][x][1]
            elif k==1:
                if y-1 <0 or x-1 < 0 :continue
                if a[y-1][x] ==0 and a[y][x] ==0 and a[y][x-1]==0:
                    d[y][x][1] += d[y-1][x-1][0] + d[y-1][x-1][1] + d[y-1][x-1][2]
            elif k==2:
                if x-1 <0 :continue
                if a[y][x] == 0:
                    d[y][x][2] += d[y][x-1][2] + d[y][x-1][1]

ans = 0

for i in range(3):
    ans +=d[N-1][N-1][i]

print(ans)
m,n = map(int,input().split())
N = int(input())
infos = []
for _ in range(N):
    direction,r = map(int,input().split())
    if direction == 1:
        infos.append((r,n,1))
    elif direction==2:
        infos.append((r,0,2))
    elif direction==3:
        infos.append((0,n-r,3))
    else:
        infos.append((m,n-r,4))
start_direction,start_r = map(int,input().split())
sx,sy =0,0

if start_direction == 1:
    sx,sy = start_r,n

elif start_direction == 2:
    sx,sy = start_r,0

elif start_direction == 3:
    sx, sy = 0,n-start_r

else:sx, sy = m, n - start_r

answer = 0
for xi,yi,d in infos:
    dist = 0
    if d + start_direction == 3 or d + start_direction == 7:
        dist = min(sx+xi+n,2*(m+n)-(sx+xi+n))
    else:
        dist+=abs(sx-xi) + abs(sy-yi)
    answer+=dist

print(answer)
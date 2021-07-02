from collections import deque
x,k = map(int,input().split())
MAX = 500000
dist = [[-1]*2 for _ in range(MAX+1)]
q = deque()
dist[x][0] = 0
q.append((x,0))

#수빈이 거리 표기
while q:
    now,t = q.popleft()
    for v in [now-1,now+1,now*2]:
        if 0<=v<=MAX:
            if dist[v][(t+1)%2]==-1:
                dist[v][(t+1)%2] = dist[now][t%2]+1
                q.append((v,t+1))
#동생의 모험
ans = -1
t = 0
while True:
    k += t
    if k > 500000:break
    if dist[k][t%2] <= t:
        ans = t
        break
    t += 1
print(ans)
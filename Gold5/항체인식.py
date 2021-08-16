n,m = map(int,input().split())

a1 = [list(map(int,input().split()))for _ in range(n)]
a2 = [list(map(int,input().split()))for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

diff_i = -1
diff_j = -1
origin_num = -1
changed_num = -1
find = False
for i in range(n):
    for j in range(m):
        if a1[i][j]!=a2[i][j]:
            diff_i, diff_j = i,j
            origin_num ,changed_num= a1[i][j],a2[i][j]
            find = True
            break
    if find:break

if not find:
    print("YES")
    exit(0)

q = []
visited = [[False]*m for _ in range(n)]
visited[diff_i][diff_j] = True
a1[diff_i][diff_j] = changed_num
q.append((diff_i,diff_j))
while q:
    y,x = q.pop()

    for k in range(4):
        ny,nx = y+ dy[k],x+dx[k]
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and a1[ny][nx]==origin_num:
            a1[ny][nx] = changed_num
            visited[ny][nx] = True
            q.append((ny,nx))

Success = True
for i in range(n):
    for j in range(m):
        if a1[i][j]!=a2[i][j]:
            Success = False
if Success:print("YES")
else:print("NO")
import copy
def inside(y_,x_):
    return 0<=y_<N and 0<=x_<N
N = 3
dy = [-1,1,0,0]
dx = [0,0,-1,1]
board = [list(map(int,input().split()))for _ in range(N)]
start = ""
end = "123456780"
for i in range(N):
    for j in range(N):
        start+=str(board[i][j])
q = [(start,0)]
hash_table = dict()
hash_table[start] = True
ans = -1
while q:
    now,cnt = q.pop(0)
    if now == end:
        ans = cnt
        break
    z = now.find("0")
    y,x = z//N,z%N

    for k in range(4):
        ny,nx = y+dy[k],x + dx[k]
        if not inside(ny,nx):continue
        nz = ny*N + nx
        next_board = list(now)
        next_board[nz],next_board[z] = next_board[z],next_board[nz]
        nextstring = ''.join(next_board)
        if not hash_table.get(nextstring):
            hash_table[nextstring]=True
            q.append((nextstring,cnt+1))
print(ans)
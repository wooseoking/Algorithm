import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

n,m,Const_K = map(int,input().split())
sharks_location = [list(map(int,input().split())) for _ in range(n)]
smell = [[0]*n for _ in range(n)]
sharks = {}
initd = [0] + list(map(int,input().split()))
whos_smell = copy.deepcopy(sharks_location)

for i in range(1,m+1):
    initd[i]-=1
for i in range(n):
    for j in range(n):
        if sharks_location[i][j]==0:continue
        who = sharks_location[i][j]
        d = initd[who]
        sharks[who] = [i,j,d]

priority_direction = [[[] for _ in range(4)] for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(4):
        priority_direction[i][j] = list(map(int,input().split()))
        for k in range(4):
            priority_direction[i][j][k]-=1

for who in sharks:
    y,x = sharks[who][0],sharks[who][1]
    smell[y][x] = Const_K

def printinfo():
    print('-------상어의 위치--------')
    for rows in sharks_location:
        print(*rows, sep=' ')
    print('-------냄새의 양--------')
    for rows in smell:
        print(*rows,sep= ' ')
    print('-------냄새의 주인--------')
    for rows in whos_smell:
        print(*rows, sep=' ')

def inside(y,x):
    return 0<=y<n and 0<=x<n

cnt = 0

while cnt!=1001:
    if len(sharks)==1:
        print(cnt)
        exit(0)
    #현재 위치 상어들 냄새 뿌리기
    for who in sharks:
        y,x = sharks[who][0],sharks[who][1]
        smell[y][x] = Const_K
    new_locations = []


    #상어의 위치 옮기기
    shark_candi = list(sharks.keys())
    shark_candi.sort()
    die = False
    find = False

    for who in shark_candi:
        y,x,d = sharks[who][0],sharks[who][1],sharks[who][2]
        die = False
        find = False
        for t in range(4):
            nd = priority_direction[who][d][t]
            ny,nx = y+dy[nd],x+dx[nd]
            if not inside(ny,nx):continue

            if smell[ny][nx] == 0:
                #알맞은 위치 찾은경우
                if sharks_location[ny][nx]==0:
                    find = True
                    sharks[who] = [ny,nx,nd]
                    sharks_location[ny][nx] = who
                    sharks_location[y][x] = 0
                    whos_smell[ny][nx] = who
                    new_locations.append((ny,nx,who))
                    break
                # 뒤지는 경우
                else:
                    del sharks[who]
                    sharks_location[y][x] = 0
                    die = True
                    break


        if die or find:continue

        for t in range(4):
            nd = priority_direction[who][d][t]
            ny,nx = y+dy[nd],x+dx[nd]
            if not inside(ny,nx):continue
            if whos_smell[ny][nx] == who:
                sharks_location[y][x] = 0
                sharks_location[ny][nx] = who
                sharks[who] = [ny,nx,nd]
                new_locations.append((ny,nx,who))
                break

    for i in range(n):
        for j in range(n):
            if smell[i][j]>0:smell[i][j]-=1
            if smell[i][j]==0:whos_smell[i][j]=0
    for y,x,who in new_locations:
        smell[y][x] = Const_K
        whos_smell[y][x] = who


    cnt+=1
print(-1)
N = int(input())
a = [[0]*N for _ in range(N)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
infos = [[]for _ in range(N*N+1)]

def inside(y_,x_):
    return 0<=y_<N and 0<=x_<N

def caculate():
    ans = 0
    for i in range(N):
        for j in range(N):
            who = a[i][j]
            whoslist = infos[who]
            cnt = 0
            for k in range(4):
                ny,nx = i+dy[k],j+dx[k]
                if not inside(ny,nx):continue
                if a[ny][nx] in whoslist:cnt+=1
            if cnt==1:ans+=1
            elif cnt==2:ans+=10
            elif cnt==3:ans+=100
            elif cnt==4:ans+=1000
    return ans

for _ in range(N*N):
    info = list(map(int,input().split()))
    num = info[0]
    like = info[1:]
    infos[num] = like
    y,x =-1,-1
    first=[]

    for i in range(N):
        for j in range(N):
            if a[i][j]==0:
                cnt = 0
                for k in range(4):
                    ny,nx = i+dy[k],j+dx[k]
                    if not inside(ny,nx):continue
                    if a[ny][nx]!=0 and (a[ny][nx] in like):cnt+=1
                first.append((cnt,i,j))
    first.sort(reverse=True)
    first_m = 0
    for cnt,i,j in first:
        if first_m <=cnt:first_m = cnt
    first_result = []
    for cnt,i,j in first:
        if cnt==first_m:first_result.append((i,j))
    if len(first_result)==1:
        y,x = first_result[0]
    else:
        second = []
        for i,j in first_result:
            cnt = 0
            for k in range(4):
                ny,nx = i+dy[k],j+dx[k]
                if not inside(ny,nx):continue
                if a[ny][nx]==0:cnt+=1
            second.append((cnt,i,j))
        second_result = []
        second.sort(reverse = True)
        second_m = 0
        for cnt , i , j in second:
            if second_m<=cnt:second_m = cnt
        for cnt,i,j in second:
            if cnt==second_m:second_result.append((i,j))
        if len(second_result)==1:
            y,x = second_result[0]
        else:
            second_result.sort()
            y,x = second_result[0]
    a[y][x] = num

print(caculate())
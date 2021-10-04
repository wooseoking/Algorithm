import copy
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

def inside(y,x):
    return 0<=y<n and 0<=x<n

n  = int(input())
a = [list(input()) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if a[i][j]=='.':
            a[i][j] = 'B'
            count = 0
            for k in range(8):
                ny,nx = i+dy[k],j+dx[k]
                success = False
                cnt = 0
                while inside(ny,nx):
                    #흰색일경우
                    if a[ny][nx]=='W':
                        cnt+=1
                        ny+=dy[k]
                        nx+=dx[k]
                    #검은색일경우
                    elif a[ny][nx]=='B':
                        success = True
                        break
                    #'.'일경우
                    elif a[ny][nx]=='.':break

                if success:count+=cnt
            a[i][j] = '.'
            result.append((count,i,j))

if result :
    result.sort(key= lambda x:(-x[0],x[1],x[2]))
    ans,ay,ax = result[0]
    if ans == 0:print("PASS")
    else:
        print(ax,ay)
        print(ans)
else : print("PASS")
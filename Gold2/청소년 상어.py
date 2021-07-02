import copy
import sys
sys.setrecursionlimit(10**9)
n =4
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]
direction = [[0]*n for _ in range(n)]
nums = [[0]*n for _ in range(n)]
nums[0][0]=-1
ans = []

def inside(y,x):
    return 0<=y<n and 0<=x<n

def movefish(Dir, Nums):
    for who in range(1,17):
        ok = False
        for i in range(n):
            for j in range(n):
                if Nums[i][j]==who:
                    y,x = i,j
                    for _ in range(8):
                        ny,nx = y + dy[Dir[y][x]], x + dx[Dir[y][x]]
                        if inside(ny,nx) and Nums[ny][nx]>=0:
                            Nums[ny][nx], Nums[y][x] = Nums[y][x], Nums[ny][nx]
                            Dir[ny][nx], Dir[y][x] = Dir[y][x], Dir[ny][nx]
                            ok = True
                            break
                        Dir[y][x]+=1
                        Dir[y][x]%=8
                if ok:break
            if ok:break

def go(y,x,Dir,Nums,cnt):
    global ans
    movefish(Dir, Nums)
    k = Dir[y][x]
    next_ = []
    ny,nx = y,x
    for _ in range(3):
        ny+=dy[k]
        nx+=dx[k]
        if inside(ny,nx) and Nums[ny][nx]>=1:
            next_.append((ny,nx))
    if len(next_)==0:
        if ans < cnt:
            ans = cnt
        return

    for ny,nx in next_:
        N_dir = copy.deepcopy(Dir)
        N_Nums = copy.deepcopy(Nums)
        N = N_Nums[ny][nx]
        N_Nums[y][x] = 0
        N_Nums[ny][nx]=-1
        go(ny,nx,N_dir,N_Nums,cnt+N)


if __name__ == "__main__":
    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in range(n):
            num,d = tmp[2*j],tmp[2*j+1]
            nums[i][j] = num
            direction[i][j] = d-1
    first = nums[0][0]

    ans = -1
    nums[0][0]=-1
    go(0,0,direction,nums,first)
    print(ans)
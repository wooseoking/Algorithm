def getdiff(tmp,ref):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if ref[i][j]!=tmp[i][j]:cnt+=1
    return cnt

def inside(y,x):
    return 0<=y<n and 0<=x<m

n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
s1 = ['B','W']
s2 = ['W','B']
ref1 = [[] for _ in range(8)]
ref2 = [[] for _ in range(8)]
for i in range(8):
    if i%2==0:
        ref1[i] = s1*4
        ref2[i] = s2*4
    else:
        ref1[i] = s2*4
        ref2[i] = s1*4

res = []

for y in range(n-7):
    for x in range(m-7):
        tmp = [rows[x:x+8] for rows in a[y:y+8]]
        cnt = 0
        res.append(getdiff(tmp,ref1))
        res.append(getdiff(tmp,ref2))
print(min(res))
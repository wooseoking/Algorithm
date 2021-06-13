import math

t = int(input())
def getEle(x):
    cnt =0
    if x==1:return 1
    for ele in range(1,math.floor(math.sqrt(x))+1):
        if x%ele==0:
            cnt+=2
    if math.sqrt(x) * math.sqrt(x) == x:cnt-=1
    return cnt

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for v in a:
        count = getEle(v)
        b.append((v,count))
    b.sort(key=lambda l:l[1],reverse=True)
    ans =0
    for i in range(n-1):
        for j in range(i+1,n):
            if math.gcd(b[i][0],2*b[j][0])>1:ans+=1
    print(ans)
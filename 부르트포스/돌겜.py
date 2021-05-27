a = [0 for _ in range(10000)]

idx = 1
num = 1
while True:
    if idx>=1000:break
    for i in range(idx,idx+num):
        a[i] = num
    idx+=num
    num+=1

ans = 0
x,y = map(int,input().split())
for i in range(x,y+1):
    ans+=a[i]
print(ans)


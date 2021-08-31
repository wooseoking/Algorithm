n,k = map(int,input().split())
query = []
for _ in range(n):
    country,g,s,b = map(int,input().split())
    query.append((country,g,s,b))
query.sort(key = lambda x:(-x[1],-x[2],-x[3]))
idx = -1
for i in range(n):
    if query[i][0] == k:
        idx = i
        break
#idx 번째에 k country 존재
it = idx -1
cnt = 0
g,s,b = query[idx][1],query[idx][2],query[idx][3]
while True:
    if it==-1:break
    g1,s1,b1 = query[it][1],query[it][2],query[it][3]
    if g1==g and s1==s and b1==b:
        it-=1
        cnt+=1
    else:break
print(idx + 1 - cnt)
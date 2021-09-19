n = int(input())
strs = []
for _ in range(n):
    strs.append(list(input()))
m = len(strs[0])
ans = ''
for j in range(m):
    c = strs[0][j]
    ok = True
    for i in range(n):
        if strs[i][j]!=c:
            ok = False
    if ok:ans+=c
    else:ans+='?'
print(ans)
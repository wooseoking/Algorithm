n = int(input())
query = input().strip()
JAV = {"J","A","V"}
ans = ""
for v in query:
    if v not in JAV:
        ans+=v
if len(ans)==0:print("nojava")
else:print(ans)
t = int(input())
for _ in range(t):
    query = list(input().split('+'))
    if len(query)==2:
        ans = sum(map(int,query))
        print(ans)
    else:
        print('skipped')

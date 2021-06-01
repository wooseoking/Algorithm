t = int(input())
for _ in range(t):
    query = input().strip()
    n = len(query)
    if n <= 10:
        print(query)
        continue
    cnt = str(n-2)
    ans = query[0] + cnt + query[n-1]
    print(ans)
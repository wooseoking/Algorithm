t = int(input())
for _ in range(t):
    start = input()
    q = []
    table = {}
    q.append((start,0))
    table[start] = True
    ans = 0
    while q:
        now,cnt = q.pop(0)
        if int(now)%25 ==0:
            ans = cnt
            break

        L = len(now)
        for i in range(L):
            next_num_str = now[:i] + now[i+1:]
            if not next_num_str:continue
            if int(next_num_str) in table:continue
            table[int(next_num_str)] = True
            next_num = str(int(next_num_str))
            q.append((next_num,cnt+1))
    print(ans)

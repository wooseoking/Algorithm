from collections import deque

arr = [[]for _ in range(61)]
dt = [60,10,-10,1,-1]

for i in range(60):
    q = deque()
    q.append((0, 0, 0, 0, 0, 0))
    visited = set()

    while q:
        addh, addt, mint, addo, mino, T = q.popleft()
        if (T == i):
            arr[i] = (addh, addt, mint, addo, mino)
            break

        for k in range(4, -1, -1):
            nextT = T + dt[k]
            if nextT not in visited:
                if nextT < 0: nextT = 0
                visited.add(nextT)
                if k == 0:
                    q.append((addh + 1, addt, mint, addo, mino, nextT))
                if k == 1:
                    q.append((addh, addt + 1, mint, addo, mino, nextT))
                if k == 2:
                    q.append((addh, addt, mint + 1, addo, mino,  nextT))
                if k == 3:
                    q.append((addh, addt, mint, addo + 1, mino,  nextT))
                if k == 4:
                    q.append((addh, addt, mint, addo, mino + 1,  nextT))

t  = int(input())
for _ in range(t):
    num = int(input())
    Q,R = divmod(num,60)
    for i in range(len(arr[R])):
        if i ==0:
            print(arr[R][i] + Q,end=' ')
        else:print(arr[R][i] ,end=' ')
    print()
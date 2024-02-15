n = int(input())
t , p = [],[]
MAX_DAY = n

for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

res = []
def solve(curDay,idx,pay):

    if curDay > n:return

    if curDay == n:
        res.append(pay)
        return

    if idx == n:
        res.append(pay)
        return

    takeTime = t[idx]
    payment = p[idx]

    solve(curDay + takeTime,idx + t[idx],pay + payment)
    solve(curDay + 1,idx + 1,pay)

solve(0,0,0)
print(max(res))
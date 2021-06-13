n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
c = [False]*n
table = set()
arr = []
def go(cnt):
    if cnt == m:
        temp = ""
        for v in arr:
            temp+=str(v)
        if temp not in table:
            table.add(temp)
            for v in arr:
                print(v,end=' ')
            print()
        return
    for i in range(len(a)):
        if c[i]:continue
        c[i] = True
        arr.append(a[i])
        go(cnt+1)
        c[i] = False
        arr.pop()
go(0)
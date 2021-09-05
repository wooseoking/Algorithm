d = []
a,p = map(int,input().split())
d.append(a)

while True:
    dn = str(d[-1])
    newnum = 0
    for v in dn:
        num = int(v)
        newnum+=num**p
    idx = 0
    if newnum in d:
        idx = d.index(newnum)
        duple = d[idx:]
        answer = [v for v in d if v not in duple]
        print(len(answer))
        break
    else:d.append(newnum)

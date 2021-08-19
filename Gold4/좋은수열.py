n = int(input())
result = []

def check(r):
    N = len(r)//2
    idx = len(r)-1
    length = 1
    if not r:return True
    for _ in range(N):
        s1 = ''.join(map(str,r[idx:idx+length]))
        s2 = ''.join(map(str,r[idx-length:idx]))
        if s1==s2:return False
        length+=1
        idx-=1
    return True

def go(r):
    if len(r)==n:
        for v in r:
            print(v,end='')
        exit(0)
        return

    for i in range(1,3+1):
        r.append(i)
        if check(r):go(r)
        r.pop(-1)
    return

go(result)
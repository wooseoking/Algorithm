def go(cadi,r):
    global A,B

    if len(cadi) == 1:
        print(-1)
        return
    next_candi = []
    L = len(cadi)

    for i in range(0,L,2):
        if i==L-1:next_candi.append(cadi[i])
        else:
            v1,v2 = cadi[i],cadi[i+1]
            if v1==A and v2==B:
                print(r)
                return
            else:
                if v2 in SET:next_candi.append(v2)
                else:next_candi.append(v1)


    go(next_candi,r+1)


N,A,B = map(int,input().split())
SET = set()
SET.add(A)
SET.add(B)
if A > B: A,B = B,A

can = [i for i in range(1,N+1)]
ans = -1
if N%2==0: N /=2
else: N = N//2+1
go(can,1)
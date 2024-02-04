import copy
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    visit = set()
    start = ''.join(map(str,a))
    visit.add(start)
    q = deque()

    q.append((start,0,total))
    ans = -1
    while q:
        now ,cnt ,s= q.popleft()

        if s == 0:
            ans = cnt
            break



        for i in range(n):
            for j in range(i,n):
                if i == j :continue

                if now[i] == now[j]:
                    tmp = list(copy.deepcopy(now))

                    #i번째 바꾸기
                    next1= copy.deepcopy(tmp)
                    n1 = int(now[i])
                    next1[i] = '0'
                    #j번째 바꾸기
                    next2 = copy.deepcopy(tmp)
                    next2[j] = '0'
                    n2 = int(now[j])
                    str_n1,str_n2 = ''.join(next1),''.join(next2)
                    if str_n1 not in visit:
                        visit.add(str_n1)
                        q.append((str_n1,cnt+1,s - n1))
                    if str_n2 not in visit:
                        visit.add(str_n2)
                        q.append((str_n2,cnt+1,s-n2))
                else:
                    min_ = min(now[i],now[j])
                    next3 = list(copy.deepcopy(now))
                    next3[i] = min_
                    next3[j] = min_
                    n3 = int(next3[i])
                    str_n3 = ''.join(next3)
                    if str_n3 not in visit:
                        visit.add(str_n3)
                        q.append((str_n3,cnt+1,s-2*n3))



    print(ans)
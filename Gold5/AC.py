import sys,re
from collections import deque
t = int(input())
for _ in range(t):
    query = list(input().strip())
    n = int(input())
    input_ = sys.stdin.readline()
    l = re.split("\[|\]|,|\n", input_)
    l = deque(l[1:-2])

    #0처리
    Error = False
    if n==0:
        for v in query:
            if v=="D":
                Error = True
        if Error:
            print("error")
        else:
            print("[]")
        continue
    Same = True
    Fail = False
    for v in query:
        if v=='D':
            if not l:
                Fail = True
                break

            if Same:
                l.popleft()
            if not Same:
                l.pop()
        else:
            Same = not Same
    if Fail:
        print("error")
    else:
        if not Same:l.reverse()
        print("[",end='')
        print(",".join(l),end='')
        print("]")
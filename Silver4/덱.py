from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    operator = input().split()
    if operator[0] == "push_front":
        q.appendleft(operator[1])
    elif operator[0] == "push_back":
        q.append(operator[1])
    elif operator[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif operator[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif operator[0] == "size":
        print(len(q))
    elif operator[0] == "empty":
        if len(q) ==0:
            print(1)
        else:
            print(0)
    elif operator[0] == "front":
        if q: print(q[0])
        else :print(-1)
    elif operator[0] == "back":
        if q: print(q[-1])
        else :print(-1)
from collections import deque
import sys
input = sys.stdin.readline

def go(a, b):
    q = deque()
    visited = set()
    state = ""
    ans = ""
    q.append((a, state))
    visited.add(a)
    while q:
        now, state = q.popleft()
        if now == b:
            ans = state
            break
        # D
        next1 = D(now)
        if next1 not in visited:
            visited.add(next1)
            q.append((next1, state + "D"))
        # S
        next2 = S(now)
        if next2 not in visited:
            visited.add(next2)
            q.append((next2, state + "S"))
        # L
        next3 = L(now)
        if next3 not in visited:
            visited.add(next3)
            q.append((next3, state + "L"))
        # R
        next4 = R(now)
        if next4 not in visited:
            visited.add(next4)
            q.append((next4, state + "R"))

    return str(ans)


def D(n):
    n = 2 * n
    if n > 9999:
        return n % 10000
    return n

def S(n):
    n -= 1
    if n <0: return 9999
    return n

def L(n):
    left = n//1000
    right = n%1000
    right = right*10 + left
    return right

def R(n):
    temp = n %10
    n = n//10
    n = temp*1000 + n
    return n

t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    ret = go(A, B)
    print(ret)
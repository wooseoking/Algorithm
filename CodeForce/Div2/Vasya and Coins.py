t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    n = 1 + a + 2*b
    if a == 0:print(1)
    else:print(n)
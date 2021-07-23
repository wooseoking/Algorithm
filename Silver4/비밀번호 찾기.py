n,m = map(int,input().split())
table = dict()
for _ in range(n):
    x,y = input().split()
    table[x] = y
for _ in range(m):
    print(table[input().rstrip()])
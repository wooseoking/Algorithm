minus = []
plus = []
result = []
cur = 0
for _ in range(4):
    m,p = map(int,input().split())
    cur += -m + p
    result.append(cur)
print(max(result))
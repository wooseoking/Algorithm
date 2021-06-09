import itertools
from string import ascii_lowercase
n,k = map(int,input().split())
temp = "antic"
a = list(v for v in ascii_lowercase if v not in temp)
word_tables = []
for _ in range(n):
    word = input().strip()
    word_table = set()
    for v in word:
        if v in temp:continue
        word_table.add(v)
    word_tables.append(word_table)
if k<5:
    print(0)
    exit(0)
ans = -1
for candidate in list(itertools.combinations(a,k-5)):
    ok = True
    cnt = 0
    candidate = set(candidate)
    for word_table in word_tables:
        if len(word_table - candidate) ==0:cnt+=1
    ans = max(cnt,ans)
print(ans)
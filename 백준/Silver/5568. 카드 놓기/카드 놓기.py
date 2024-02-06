import itertools

n = int(input())
k = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
res = set()
for s in itertools.permutations(a,k):
    res.add(int(''.join(map(str,s))))
print(len(res))
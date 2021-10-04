import bisect

n = int(input())
a = list(map(int,input().split()))

result = []

for v in a:
    if not result or result[-1] < v:
        result.append(v)

    idx = bisect.bisect_left(result,v)
    result[idx] = v
print(len(result))
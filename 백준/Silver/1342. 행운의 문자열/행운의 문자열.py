from collections import Counter
a = list(input())
n = len(a)
cnt = Counter(a)

def solve(pre,depth):
    answer = 0

    if depth == n:
        return 1

    for key in cnt.keys():
        if cnt[key] == 0 or key == pre:continue
        cnt[key] -= 1
        answer += solve(key, depth + 1)
        cnt[key] += 1
    return answer

print(solve('',0))

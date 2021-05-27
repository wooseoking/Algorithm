import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
sets = list(sorted(set(a)))

dic = {v : i for i ,v in enumerate(sets)}
for c in a:
    print(dic[c])

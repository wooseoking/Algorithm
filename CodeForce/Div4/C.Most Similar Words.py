tc = int(input())

def caculate(w1,w2):
    sum = 0
    for s1,s2 in zip(w1,w2):
        sum+= abs(ord(s1) - ord(s2))
    return sum

for _ in range(tc):
    n,m = map(int,input().split())
    words = []
    for _ in range(n):
        words.append(input())
    res = []

    for i in range(n):
        for j in range(i,n):
            if i == j:continue
            s1,s2 = words[i],words[j]
            res.append(caculate(s1,s2))
    print(min(res))
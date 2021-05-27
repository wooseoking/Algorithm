import math
a,b,c,d = map(str,input().split())
table = {a: 0.0, b: 0.0, c: 0.0, d: 0.0}
for _ in range(6):
    x,y,s1,s2,s3 = map(str,input().split())
    n1 = float(s1)
    n2 = float(s2)
    n3 = float(s3)
    table[x]+=n1*3
    table[x]+=n2*1
    table[y]+=n2*1
    table[y]+=n3*3

arr = []
for team in table.keys():
    arr.append((team,table[team]))
print(arr)
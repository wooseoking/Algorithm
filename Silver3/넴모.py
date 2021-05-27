import math
import itertools
n = int(input())
cnt = 0
res = []
digits = [9-v for v in range(0,10)]

for i in range(1,11):
    arr = list(itertools.combinations(digits,i))
    temp = []
    for v in arr:
        number = ""
        for ele in v:
            number +=str(ele)
        temp.append(int(number))
    res+=temp
res.sort()
if n<len(res):print(res[n])
else :print(-1)
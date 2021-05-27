import itertools
num = int(input())
a = list(map(int,str(num).strip()))
a.sort()
U = list(itertools.permutations(a,len(a)))
ans = 0
for val in U:
    temp = ""
    for n in val:
        temp+=str(n)
    if int(temp) > num:
        ans = int(temp)
        break
print(ans)
def generateIOI(n):
    ret = ""
    query = "IO"
    for _ in range(n):
        ret+=query
    ret+="I"
    return ret
def makeTable(pattern):
    l = len(pattern)
    table = [0]*l
    j = 0
    for i in range(1,l):
        while j>0 and pattern[i]!=pattern[j]:
            j = table[j-1]
        if pattern[i]==pattern[j]:
            table[i] = j+1
            j+=1
    return table

n = int(input().strip())
l = int(input().strip())
parent = input().strip()
pattern = generateIOI(n)
table = makeTable(pattern)
parentSize= len(parent)
patternSize = len(pattern)
j = 0
ans = 0

for i in range(parentSize):
    while j>0 and parent[i]!=pattern[j]:
        j = table[j-1]
    if parent[i]==pattern[j]:
        #i - patterSize +2 에서 찾음
        if j == patternSize -1:
            j = table[j]
            ans+=1
        else : j+=1
print(ans)
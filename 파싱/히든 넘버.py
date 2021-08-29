n = int(input())
a = input().rstrip()
result = []
tmp = ''
for v in a:
    if '0'<=v<='9':
        tmp+=v
    else:
        if not tmp:continue
        result.append(int(tmp))
        tmp = ''
if tmp:
    result.append(int(tmp))
if not result:print(0)
else:print(sum(result))
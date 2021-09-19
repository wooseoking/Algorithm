string = input()
n = len(string)
result = []
for i in range(n):
    tmp = string[i:]
    result.append(tmp)
result.sort()
for v in result:
    print(v)
t = int(input())
for _ in range(t):
    query = list(input().split())
    table = dict()
    result = []
    while True:
        string = input()
        if string == 'what does the fox say?':break
        animal,to,say = map(str,string.split())
        table[say] = True
    for x in query:
        if x not in table:
            result.append(x)
    for v in result:
        print(v,end=' ')
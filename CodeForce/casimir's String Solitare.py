t = int(input())
for _ in range(t):
    query = list(input())
    table = {'A': 0, 'B': 0, 'C': 0}

    for v in query:
        table[v]+=1

    print('YES' if table['A'] + table['C'] == table['B'] else 'NO')
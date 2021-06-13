n = int(input())
table = set()
for _ in range(n):
    name, state = input().split()
    if state =="enter":table.add(name)
    else :
        if name in table:
            table.remove(name)

ans_list = list(table)
ans_list.sort(reverse=True)
for name in ans_list:
    print(name)
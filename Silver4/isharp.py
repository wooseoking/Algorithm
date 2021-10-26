query = list(input().split(' '))
f = query[0]
n = len(query)
for i in range(1,n):
    var = ''
    idx = 0
    for j in range(len(query[i])):
        if query[i][j].isalpha():var+=query[i][j]
        else:
            idx = j
            break

    
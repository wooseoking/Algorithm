n,m = map(int,input().split())
a = [list(map(int,input())) for _ in range(n)]
res = []

# Bitmasking 0 : 가로 , 1 : 세로
for s in range(1 << n * m):
    #가로
    widths = 0
    for i in range(n):
        width = 0

        for j in range(m):
            z = i * m + j
            if s & (1 << z) == 0:
                width = width * 10 + a[i][j]
            else:
                widths += width
                width = 0
        widths += width

    heights = 0
    for j in range(m):
        height = 0
        for i in range(n):
            z = i * m + j
            if s & (1 << z) != 0 :
                height = height * 10 + a[i][j]
            else:
                heights += height
                height = 0

        heights += height

    res.append(widths + heights)

print(max(res))
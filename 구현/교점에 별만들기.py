def solution(line):
    INF = float('inf')
    points, L = [], len(line)
    minx, maxx, miny, maxy = INF, -INF, INF, -INF
    for i in range(L):
        for j in range(i, L):
            if i == j: continue
            A, B, E = line[i][0],line[i][1],line[i][2]
            C, D, F = line[j][0],line[j][1],line[j][2]
            d = A * D - B * C
            if d == 0: continue
            x, y = (B * F - E * D) / d, (E * C - A * F) / d
            if x - int(x) or y - int(y): continue
            x, y = int(x), int(y)
            minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
            points.append((x, y))

    N = maxy - miny +1
    M = maxx - minx +1
    ans = [['.' for _ in range(M)] for _ in range(N)]
    for x, y in points: ans[maxy - y][x - minx] = '*'
    return [''.join(rows) for rows in ans]
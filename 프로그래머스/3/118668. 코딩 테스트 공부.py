import heapq
import math

def dijikstra(sx,sy,ex,ey,problems):
    q = []
    heapq.heappush(q,[0,sx,sy])
    d = [[math.inf] * (ey + 1) for _ in range(ex + 1)]
    d[sx][sy] = 0

    while q:
        cost,x,y = heapq.heappop(q)

        if d[x][y] < cost: continue

        if x + 1 < ex + 1:
            nextCost = d[x][y] + 1

            if nextCost < d[x + 1][y]:
                d[x + 1][y] = nextCost
                heapq.heappush(q,[nextCost,x + 1,y])

        if y + 1 < ey + 1:
            nextCost = d[x][y] + 1
            if nextCost < d[x][y + 1]:
                d[x][y + 1] = nextCost
                heapq.heappush(q, [nextCost, x, y + 1])

        for alp_req,cop_req,alp_rwd,cop_rwd,c in problems:

            if x >= alp_req and y >= cop_req:
                nextX = min(ex,x + alp_rwd)
                nextY = min(ey,y + cop_rwd)
                nextCost = d[x][y] + c
                if nextCost < d[nextX][nextY]:
                    d[nextX][nextY] = nextCost
                    heapq.heappush(q,[nextCost,nextX,nextY])

    return d[-1][-1]

def solution(alp,cop,problems):
    max_alp = max(alp,max(p[0] for p in problems))
    max_cop = max(cop,max(p[1] for p in problems))

    answer = dijikstra(alp,cop,max_alp,max_cop,problems)
    return answer
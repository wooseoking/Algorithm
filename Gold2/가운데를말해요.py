import sys
import heapq
input = sys.stdin.readline
n = int(input())
left_pq = []
right_pq = []

for _ in range(n):
    if len(left_pq) == len(right_pq): heapq.heappush(left_pq,-int(input()))
    else : heapq.heappush(right_pq,int(input()))

    if len(right_pq)==0:
        print(-left_pq[0])
        continue

    l = -left_pq[0]
    r = right_pq[0]
    if l > r:
        heapq.heappop(left_pq)
        heapq.heappop(right_pq)
        heapq.heappush(left_pq,-r)
        heapq.heappush(right_pq,l)
    print(-left_pq[0])
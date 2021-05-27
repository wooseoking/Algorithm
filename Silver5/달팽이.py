import sys
import heapq
input = sys.stdin.readline
n = int(input())
stack = []
pq = []
for _ in range(n):
    heapq.heappush(pq,int(input()))
ans = 0

while pq:
    now = heapq.heappop(pq)
    if stack:
        temp = stack.pop(0)
        temp+=now
        heapq.heappush(pq,temp)
        ans +=temp
        stack.clear()
    else:
        stack.append(now)
print(ans)
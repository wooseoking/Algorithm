import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    pq = []
    for _ in range(n):
        op,num = input().split()
        num = int(num)
        if op=='I':
            heapq.heappush(pq,num)
        else:
            if not pq:continue
            if num==-1:#최소값
                heapq.heappop(pq)
            else:#최대값
                pq.pop(pq.index(heapq.nlargest(1,pq)[0]))
    if not pq:print('EMPTY')
    else:
        print(heapq.nlargest(1,pq)[0],heapq.nsmallest(1,pq)[0])
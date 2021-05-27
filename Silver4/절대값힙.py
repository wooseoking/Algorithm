import heapq
def solution(jobs):
    answer = 0
    q= []
    a = jobs
    a.sort(key = lambda x : x[0])
    cur_time = a[0][0]
    count = 1
    cur_end = -1
    while count <= len(jobs):
        for start , during in jobs:
            if cur_end < start <=cur_time:
                heapq.heappush(q,(during,start))
        if q:
            count+=1
            cur_end = cur_time
            during,start = heapq.heappop(q)

    return answer
import heapq


def solution(jobs):
    jobs.sort()

    ready_queue = []

    current_time = 0
    time = 0

    # jobs 리스트의 인덱스
    n = len(jobs)

    completed_jobs = 0

    while completed_jobs < n:
        # 현재시간까지 도착한 작업을 모두 준비 큐에 추가
        while jobs and jobs[0][0] <= current_time :
            req_time , processing_time = jobs.pop(0)
            heapq.heappush(ready_queue,[processing_time,req_time])

        if ready_queue:
            processing_time,req_time = heapq.heappop(ready_queue)

            if req_time < current_time:
                current_time += processing_time
                time += current_time - req_time
            else:
                current_time = req_time + processing_time
                time += processing_time

            completed_jobs += 1

        else:
            current_time = jobs[0][0]
    
    return time // n
import heapq


def solution(jobs):

    jobs.sort()

    ready_queue = []
    current_time = 0
    completed_job = 0
    n = len(jobs)
    answer = 0

    while completed_job != n :

        # 현재 시간 기준 작업 목록 -> ready queue에 집어넣기

        while jobs and jobs[0][0] <= current_time:
            req_time,proc_time = jobs.pop(0)
            heapq.heappush(ready_queue,[proc_time,req_time])


        if ready_queue:
            proc_time , req_time = heapq.heappop(ready_queue)

            current_time += proc_time
            answer += current_time - req_time
            completed_job += 1
            print(current_time - req_time)
        else:
            current_time = jobs[0][0]


    return answer // n
import heapq
import math

cadidates = []
comb = []

def getCandidate(k,n):
    if len(comb) == k :
        if sum(comb) == n:
            cadidates.append(comb.copy())
        return

    for num in range(1,n + 1):
        comb.append(num)
        getCandidate(k,n)
        comb.pop(-1)

def getWaitingTime(n,id,table):
    runningQueue = [] #[오로지 끝나는 시간 기준] 기준으로 힙
    waitingQueue = table[id].copy()
    waitingTime = 0

    while waitingQueue:
        req = waitingQueue.pop(0)
        reqTime,duringTime = req

        # 아직 상담원이 다 안찼다면
        if len(runningQueue) < n:
            heapq.heappush(runningQueue,reqTime + duringTime)
        else:
            #다찼을 경우
            finishedTime = heapq.heappop(runningQueue)

            # 기다리는 경우
            if finishedTime > reqTime:

                waitingTime += abs(finishedTime - reqTime)
                heapq.heappush(runningQueue,finishedTime + duringTime)
            else:
                #안기다려도 되는경우
                heapq.heappush(runningQueue,reqTime + duringTime)

    return waitingTime


def solution(k, n, reqs):
    answer = 0
    # a + b + c  .. + d = n (a,b,c,d .. ) 의 개수는 k 개

    # 2. 쿼리 파싱
    requestById = dict()
    numOfId = 0
    for req in reqs:
        arrivalTime , duringTime , id = req
        endTime = arrivalTime + duringTime
        if id not in requestById:
            numOfId += 1
            requestById[id] = []
        requestById[id].append([arrivalTime,duringTime])

    # 순서쌍 찾아주자
    # 3. x 명의 삼담원이 있을때 id별 해당 기다리는 함수 로직
    # 4. id 가져오기
    ids = list(requestById.keys())
    ids.sort()
    getCandidate(k,n)
    res = []
    for candidate in cadidates:
        waitingTime = 0
        for i in range(k):
            id,c = i + 1, candidate[i]
            if id not in requestById:continue
            waitingTime += getWaitingTime(c,id,requestById)
        res.append(waitingTime)
    answer = min(res)
    return answer




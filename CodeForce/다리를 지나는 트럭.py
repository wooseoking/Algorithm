from collections import deque
def solution(bridge_length, weight, truck_weights):

    waitinglist = deque(truck_weights)
    bridge = deque()
    result = []
    N = len(truck_weights)
    t = 0
    while True:

        print(bridge)
        if len(result)==N:break
        if waitinglist and sum(bridge) + waitinglist[0] <=weight and len(bridge)<bridge_length:
            bridge.append((waitinglist.popleft()))

        if bridge and t+1 %bridge_length ==0:
            result.append(bridge.popleft())
        t+=1
    return t
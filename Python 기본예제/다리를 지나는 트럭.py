def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    while True:
        if not truck_weights:break
        answer+=1
        if sum(bridge)<=weight and len(bridge)<bridge_length:
            bridge.append(truck_weights.pop(0))
        if len(bridge)==bridge_length:
            bridge.pop(0)
    return answer
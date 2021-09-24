def solution(enter, leave):
    answer = [0]*len(enter)
    room = []
    idx = 0

    for l in leave:
        while l not in room:
            room.append(enter[idx])
            idx+=1
        room.remove(l)
        #떠나는녀석 계산
        answer[l-1]+=len(room)
        #안에있는녀석들
        for person in room:
            answer[person-1]+=1

    return answer
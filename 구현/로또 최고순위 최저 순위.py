def solution(lottos, win_nums):
    answer = []
    cnt = 0
    i_dont_know = lottos.count(0)
    for num in win_nums:
        if num in lottos:cnt+=1
    max_num = cnt + i_dont_know
    min_num = cnt
    if max_num==6:
        answer.append(1)
    elif max_num == 5:
        answer.append(2)
    elif max_num == 4:
        answer.append(3)
    elif max_num == 3:
        answer.append(4)
    elif max_num == 2:
        answer.append(5)
    else:
        answer.append(6)

    if min_num==6:
        answer.append(1)
    elif min_num == 5:
        answer.append(2)
    elif min_num == 4:
        answer.append(3)
    elif min_num == 3:
        answer.append(4)
    elif min_num == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer
def solution(scores):
    answer = 1
    oneho_score = scores[0]
    # 원호 인센 실패
    if any(other[0] > oneho_score[0] and other[1] > oneho_score[1]for other in scores):return -1
    # 인센 안받는 친구들 솎아 내기
    filtered_scores = []
    scores.sort(key = lambda x:(-x[0],x[1]))
    f1,f2 = scores[0]
    
    for n1,n2 in scores:
        if n2 >= f2:
            f2 = n2    
            filtered_scores.append([n1,n2])
    # 총합으로 큰순서대로 순위 매기기 (단 동점 수는 동일 등수 처리)

    filtered_scores.sort(reverse=True, key= lambda x: (x[0] + x[1]))

    groups = dict()

    for n1,n2 in filtered_scores:
        sum = n1 + n2
        if sum not in groups:
            groups[sum] = 1
        else:
            groups[sum] +=1

    keys = list(groups.keys())
    keys.sort(reverse=True)

    # 원호의 순서 알아내기
    oneho_sum = oneho_score[0] + oneho_score[1]

    for key in keys:
        if oneho_sum == key:break

        answer += groups[key]

    return answer
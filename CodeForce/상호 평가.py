def solution(scores):
    answer = ''
    n = len(scores)
    mean = [0]*n

    for i in range(n):
        myscore = []
        self_score = scores[i][i]
        for j in range(n):
            myscore.append(scores[j][i])
        max_s = max(myscore)
        min_s = min(myscore)
        myscore.sort()
        if max_s == self_score and myscore[n-1]!=myscore[n-2] or min_s == self_score and myscore[0]!=myscore[1]:
            mean[i] = (sum(myscore) - self_score)/(n-1)
        else:
            mean[i] = sum(myscore)/n
    for i in range(n):
        if mean[i]>=90:answer+="A"
        elif mean[i]>=80:answer+="B"
        elif mean[i]>=70:answer+="C"
        elif mean[i] >= 50:answer += "D"
        else:answer+="F"
    return answer
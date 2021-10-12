import bisect


def solution(info, query):
    answer = []
    table = []
    for d in info:
        d = d.split(' ')
        table.append(d)

    table.sort(key=lambda x:int(x[4]))
    condition = []
    scores = []
    for lang , major, ability , soulfood ,score in table:
        condition.append((lang , major, ability , soulfood))
        scores.append(int(score))
    n = len(scores)


    for sql in query:
        sql = sql.split(' and ')
        last = sql[-1]
        sql = sql[:-1]
        last = last.split(' ')
        sql+=last
        lang , major, ability , soulfood ,score = sql[0],sql[1],sql[2],sql[3],int(sql[4])
        idx = bisect.bisect_left(scores,score)

        cnt = 0
        for i in range(idx,n):
            l, m, a, soul_f = condition[i][0],condition[i][1],condition[i][2],condition[i][3]
            if (l==lang or lang=='-') and (major ==m or major=='-') and (ability == a or ability=='-') and (soulfood==soul_f or soulfood=='-'):cnt+=1
        answer.append(cnt)
    return answer
def solution(weights, head2head):
    answer = []
    table = []
    n = len(weights)
    for i in range(n):
        #승률
        win = 0
        cnt = 0
        round = 0
        for j in range(n):
            if i==j:continue
            if head2head[i][j]=='W' or head2head[i][j]=='L':round+=1
            if head2head[i][j]=='W':
                win+=1
                if weights[i] < weights[j]:cnt+=1
        if round == 0:winrate = 0
        else : winrate = win/round
        #나보다 무게무거운 복서 이긴횟수
        table.append((winrate,cnt,weights[i],i))

    table.sort(key = lambda x:(-x[0],-x[1],-x[2],x[3]))

    for v in table:
        answer.append((v[3]+1))

    return answer
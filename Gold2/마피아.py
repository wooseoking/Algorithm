ENDOFGAME = False
n = int(input())
parties = [[0]*4 for _ in range(n)]
init_r = list(map(int,input().split()))
for i_ in range(n):
    parties[i_][0] = i_ #번호
    parties[i_][1] = 0  #마피아
    parties[i_][2] = 1  #live
    parties[i_][3] = init_r[i_] #유죄지수
R = [list(map(int,input().split())) for _ in range(n)]
mafia = int(input())
parties[mafia][1] = 1

ans = -1
# 0 번호 1 마피아 2 live 3 유죄지수
def simulate(civil,day):
    global parties,ans,ENDOFGAME

    if ENDOFGAME:return
    if parties[mafia][2]==0 or civil == 0:
        ans = max(ans,day)
        if parties[mafia][2]==1 and civil == 0:
            ENDOFGAME = True
        return

    people = civil+1

    if people%2==0:
        for i in range(n):
            if parties[i][2]==0:continue
            if i==mafia:continue

            #죽여
            parties[i][2] = 0

            #유죄지수 증가
            for j in range(n):
                if parties[j][2]==0:continue
                parties[j][3] += R[i][j]

            simulate(civil-1,day+1)
            if ENDOFGAME:return
            for j in range(n):
                if parties[j][2] == 0: continue
                parties[j][3] -= R[i][j]
            parties[i][2] = 1
    else:
        candi = []
        for i in range(n):
            if parties[i][2]==0:continue
            candi.append((parties[i][3],parties[i][0]))
        candi.sort(key=lambda x:(-x[0],x[1]))
        die_num = candi[0][1]
        parties[die_num][2] = 0
        simulate(civil-1,day)
        parties[die_num][2] = 1


simulate(n-1,0)
print(ans)
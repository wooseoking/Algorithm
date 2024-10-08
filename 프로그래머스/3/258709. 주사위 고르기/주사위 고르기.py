from collections import Counter
def solution(dice):
    answer = []
    n = len(dice)

    def getAllSumOfDice(idx, sumDice, selectedDice,res):
        if idx == len(selectedDice):
            res.append(sumDice)
            return

        d = dice[selectedDice[idx]]

        for diceNumber in d:
            getAllSumOfDice(idx + 1, sumDice + diceNumber, selectedDice,res)


    # dice 를 두개의 Pair로 나누기
    combinationsA ,combinationsB= [],[]
    for i in range(1 << n):
        tmpA,tmpB = [],[]
        for j in range(n):
            if i & (1 << j) != 0:
                tmpA.append(j)
            else:
                tmpB.append(j)
        if len(tmpA) == n // 2:
            combinationsA.append(tmpA)
            combinationsB.append(tmpB)

    # 조합의 경우의 수 표
    resultChart = [[0] * 3 for _ in range(len(combinationsA))]

    # 각각의 주사위의 조합 구하기
    for i in range(len(combinationsA)):
        selectedDiceA,selectedDiceB = combinationsA[i],combinationsB[i]
        resA,resB = [],[]
        getAllSumOfDice(0, 0, selectedDiceA,resA)
        getAllSumOfDice(0, 0, selectedDiceB,resB)

        resA = Counter(resA)
        resB = Counter(resB)

        for aScore,aCount in resA.items():
            for bScore,bCount in resB.items():
                if aScore > bScore:
                    resultChart[i][0]+=aCount * bCount
                elif aScore == bScore:
                    resultChart[i][1]+=1
                else:
                    resultChart[i][2]+=1

    winRate = []
    for i in range(len(resultChart)):
        rows = resultChart[i]
        win = rows[0]
        winRate.append([win,i])

    winRate.sort(key=lambda x:-x[0])
    answerDiceIdx = winRate[0][1]
    answer = combinationsA[answerDiceIdx]
    for i in range(len(answer)):
        answer[i] +=1
    return answer

#solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])
def checkvalid(num):
    num = ''.join(x for x in num if x not in '-')
    s1 = 0

    for idx in range(len(num)-1,-1,-1):
        if (idx+1)%2==0:continue
        s = int(num[idx])*2
        if s>=10:
            s = (s//10) + (s%10)
        s1+=s
    s2 = 0
    for idx in range(len(num)-1,-1,-1):
        if (idx+1)%2==1:continue
        s2+=int(num[idx])

    return (s1+s2)%10==0

def solution(card_numbers):
    answer = []

    for cardnum in card_numbers:
        c1 = False
        c2 = False
        if len(cardnum)==16 or len(cardnum)==19:
            if len(cardnum)==16:
                ok1 = True
                for v in cardnum:
                    if not '0'<=v<='9':
                        ok1 = False
                if ok1:
                    if checkvalid(cardnum):
                        c1 = True



            elif len(cardnum)==19:
                ok2 = True
                for i in range(len(cardnum)):
                    if i==4 or i==9 or i==14:
                        if cardnum[i]!='-':
                            ok2 = False
                if ok2:
                    if checkvalid(cardnum):
                        c2 = True
        if c1 or c2:
            answer.append(1)
        else:answer.append(0)

    return answer
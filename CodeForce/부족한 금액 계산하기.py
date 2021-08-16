def solution(price, money, count):
    tot = count*(count+1)//2
    tot = tot*price
    answer = money - tot
    if answer>=0:answer=0
    else:answer=-answer
    return answer
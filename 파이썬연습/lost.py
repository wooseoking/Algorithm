import math


def getElement(n):
    result = []
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result

def solution(left, right):
    answer = 0
    for e in range(left,right+1):
        l = getElement(e)
        if len(l)%2==0:answer+=e
        else:answer-=e
    return answer

print(getElement(4))
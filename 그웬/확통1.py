def solution(arr):
    answer = -1
    result = []
    for c in range(0,255+1):
        a,b = 0,0
        for v in arr:
            if v>=c:a+=1
            elif v<=c:b+=1
        result.append((abs(a-b),c))
    result.sort()
    answer = result[0][1]
    return answer
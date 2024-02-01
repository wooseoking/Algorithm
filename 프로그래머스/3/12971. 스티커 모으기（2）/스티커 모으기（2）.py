def dp(sticker):
    n = len(sticker)
    d = [[0]*2 for _ in range(n)]
    
    d[0][0] = 0
    d[0][1] = sticker[0]
  
    for i in range(n):
        d[i][0] = max(d[i-1][0],d[i-1][1])
        d[i][1] = d[i-1][0] + sticker[i]
    
    return max(d[n-1][0],d[n-1][1])

def solution(sticker):
    if len(sticker) == 1: return sticker[0]

    if len(sticker) == 2: return max(sticker)
    a1 = dp(sticker[1:])
    a2 = dp(sticker[:-1])
    
    answer = max(a1,a2)
    return answer
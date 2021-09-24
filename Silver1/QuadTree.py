def go(arr,y,x,size):
    ok = True
    pixel = arr[y][x]
    for i in range(y,y+size):
        for j in range(x,x+size):
            if arr[i][j]!=pixel:ok = False
    if ok: return str(pixel)

    ans = "("
    next_size = size//2
    Area1 = go(arr,y,x,next_size)
    Area2 = go(arr,y,x+next_size,next_size)
    Area3 = go(arr,y+next_size,x,next_size)
    Area4 = go(arr,y+next_size,x+next_size,next_size)
    ans+=Area1
    ans+=Area2
    ans+=Area3
    ans+=Area4
    ans+=")"
    return ans

def solution(arr):
    answer = []
    ret = go(arr,0,0,len(arr))
    zero = 0
    one = 0
    for ele in ret:
        if ele == "0" : zero+=1
        elif ele == "1" : one+=1
    answer.append(zero)
    answer.append(one)
    return answer


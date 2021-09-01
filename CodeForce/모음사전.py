a = ['A','E','I','O','U']
cnt = 0
answer = 0
result = []

def go(index,word):
    global answer,cnt
    if len(result)>5:return
    if ''.join(result) == word:
        answer = cnt
        return
    cnt+=1
    for idx in range(5):
        result.append(a[idx])
        go(idx,word)
        result.pop()


def solution(word):
    go(0,word)
    return answer


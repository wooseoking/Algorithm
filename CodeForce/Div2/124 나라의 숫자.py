def solution(n):
    answer = ''
    a = ['0','1','2','4']
    stack = []
    while n!=0:
        q,r = divmod(n,3)
        stack.append(r)
        if r == 0:
            n = q-1
        else:
            n = q

    stack.reverse()

    for idx in stack:
        if idx == 0:
            answer+=a[3]
        else:
            answer+=a[idx]
    return answer
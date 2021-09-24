t = int(input())
for _ in range(t):
    a = list(input())
    left = []
    right = []
    for c in a:
        if c=='-':
            if left:
                left.pop()
        elif c=='<':
            if left:
                right.append(left.pop())
        elif c=='>':
            if right:
                left.append(right.pop())
        else:
            left.append(c)
    ans = ''.join(left)  + ''.join(reversed(right))
    print(ans)

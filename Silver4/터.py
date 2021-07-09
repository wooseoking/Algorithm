t = int(input())
for _ in range(t):
    n = int(input())
    binary = format(n,'b')
    binary = list(map(int,binary))
    binary.reverse()
    ans = 0
    for i,v in enumerate(binary):
        if v==1:
            ans+=pow(3,i)
    print(ans)
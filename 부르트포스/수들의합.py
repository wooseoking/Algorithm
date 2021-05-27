n = int(input())
ans = 1
while ans*(ans+1) < 2*n:
    ans+=1

if ans*(ans+1)==2*n:
    print(ans)
else:
    print(ans-1)
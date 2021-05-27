import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    h,w,n = map(int,input().split())
    n-=1
    HO = n//h + 1
    FLOOR = n%h +1
    ans = str(FLOOR)
    temp =str(HO)
    if 1<=HO<=9:
        ans+="0"
        ans+=temp
        print(ans)
    else:
        ans+=temp
        print(ans)
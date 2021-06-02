n = int(input())
if n==1:
    print(1)
    print(1,1)
    exit(0)

ans = 2*(n-1)
up = ans//2+1
down = ans//2-1
print(ans)
for i in range(1,up+1):
    print(1,i)
for i in range(2,2+down):
    print(n,i)

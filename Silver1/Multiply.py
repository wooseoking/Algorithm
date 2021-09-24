a,b,c = map(int,input().split())

def Power(x,n,mod):
    if n==0:return 1
    if n%2==1:
        m = (n-1)//2
        y = Power(x,m,mod)
        return x*y*y%mod
    else:
        m = n//2
        y = Power(x,m,mod)
        return y*y%mod

print(Power(a,b,c))
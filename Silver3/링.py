n = int(input())
a = list(map(int,input().split()))
result = []
parent = a[0]
def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

for i in range(1,n):
    child = a[i]
    gcd = GCD(child,parent)
    a_ = parent//gcd
    b_ = child//gcd
    print(str(a_)+"/"+str(b_))
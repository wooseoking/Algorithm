import itertools

n,m = map(int,input().split())
a = list(map(int,input().split()))
n1 = n//2
n2 = n-n1
left,right = a[0:n1],a[n1:]
L,R = [],[]

for cnt in range(0,len(left)+1):
    for s in itertools.combinations(left,cnt):
        L.append(sum(s))

for cnt in range(0,len(right)+1):
    for s in itertools.combinations(right,cnt):
        R.append(sum(s))
L.sort()
R.sort(reverse=True)
l,r = 0,0
ans = 0
n1,n2 = len(L),len(R)

while l<n1 and r<n2:
    if L[l] + R[r]==m:
        c1,c2=1,1
        l+=1
        r+=1
        while 0<=l<n1 and L[l]==L[l-1]:
            l+=1
            c1+=1
        while 0<=r<n2 and R[r]==R[r-1]:
            r+=1
            c2+=1
        ans +=c1*c2
    elif L[l] + R[r] > m:
        r+=1
    else:
        l+=1
if m==0:ans-=1
print(ans)

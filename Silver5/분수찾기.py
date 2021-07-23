k = int(input())
n = 1
while True:
    s = n*(n+1)//2
    if s>=k:
        target = (n-1)*n//2

        for i in range(1,n+1):
            if target+i==k:
                if n&1==1:
                    print(str(n-i+1)+'/'+str(i))
                else:
                    print(str(i)+'/'+str(n-i+1))
                break
        break

    n+=1
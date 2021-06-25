print("Number of scale")
n = int(input())
a = list(map(int,input().split()))
total = sum(a)
for k in range(1,n):
    total1 = 0
    total2 = 0
    for v in a[:k]:
        total1+=v
    for v in a[k:]:
        total2+=v
    m1 =total1 / total
    m2 =total2 / total
    u1 = 0
    for i in range(k):
        u1+=i*a[i]
    u1 /=total1

    u2 = 0
    for i in range(k,n):
        u2 += i*a[i]
    u2 /= total2

    sigma1= 0
    for i in range(k):
        sigma1+=(i-u1)**2*a[i]
    sigma1/=total1

    sigma2 = 0
    for i in range(k,n):
        sigma2 += (i - u2) ** 2 * a[i]
    sigma2 /= total2

    print("==========",k,"일경우============")
    print("sima1")
    print("평균:",m1)
    print("u1:",u1)
    print("sigma1:",sigma1)
    print("-----------------")
    print("sima2")
    print("평균:", m2)
    print("u2:", u2)
    print("sigma2:", sigma2)
    print("Otsu :",m1*sigma1 + m2*sigma2)

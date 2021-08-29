k = int(input())
if k>0:
    i = 0
    an= 0
    while True:
        if an>=k:break
        an = pow(2,i)-1
        i+=1
    print(i-1)
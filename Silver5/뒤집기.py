if __name__ =='__main__':
    n = 0
    a = input()
    for v1,v2 in zip(a[:],a[1:]):
        if v1!=v2:n+=1
    n+=1
    print(n//2 if n%2==0 else (n-1)//2)
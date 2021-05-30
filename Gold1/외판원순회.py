while True:
    a = list(input().strip())
    if a[0]=="0":break
    b = list(reversed(a))
    if a==b:print("yes")
    else : print("no")
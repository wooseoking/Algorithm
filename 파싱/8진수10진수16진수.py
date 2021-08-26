a = input().rstrip()
if a[0]=='0':
    if a[1]=='x':
        hexa = int(a,16)
        print(hexa)
    else:
        octa = int('0o'+a[1:],8)
        print(octa)
else:print(a)
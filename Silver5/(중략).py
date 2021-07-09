n = int(input())
string = input().strip()
number = [0]*n
num = 0
for i,c in enumerate(string):
    if c!='.':
        number[i] = num
    else:
        number[i]=num
        num+=1

if n<=25:print(string)
else:
    sublen = n-22
    ok = True
    v1 = number[11]
    for i in range(11,11+sublen):
        if v1!=number[i]: ok = False
    if ok:
        string = string[:11]+"..."+string[-11:]
        print(string)
    else:
        string = string[:9]+"......"+string[-10:]
        print(string)

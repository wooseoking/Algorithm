n = int(input())
a = list(map(int,input().split()))
if n==1:
    print("Yes")
    exit(0)
b = a[1:]
b.sort()
x = a[0]
Flag = True
for v in b:
    if x>v:
        x+=v
    else:
        Flag = False
        break
print("Yes" if Flag else "No")
def ok(n):
    if n%3==0:return False
    to_num = str(n)
    if to_num[-1]=='3':return False
    return True

a = []
num = 1
while len(a)!=1000:
    if ok(num):a.append(num)
    num+=1
t = int(input())

for _ in range(t):
    idx = int(input())
    print(a[idx-1])
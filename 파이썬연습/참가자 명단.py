n,m = map(int,input().split())
a = [[]for _ in range(n)]
while True:
    num,name = map(str,input().split())
    if num=='0' and name=='0':break
    num = int(num)-1
    if len(a[num])<m:
        a[num].append(name)
for i in range(n):
    a[i].sort(key=lambda x:(len(x),x))

result = []

for i in range(n):
    if i%2==0:
        for child in a[i]:
            result.append((i+1,child))

for i in range(n):
    if i%2==1:
        for child in a[i]:
            result.append((i+1,child))


for num,name in result:
    print(num,name)

string = input()
cnt = 0
for v in string:
    if v=='(' or v=='[':cnt+=1
    else:cnt-=1
if cnt==0:
    stack = []

else:print(0)
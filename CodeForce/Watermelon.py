w = int(input())
success = False
for w1 in range(1,101):
    for w2 in range(1,101):
        if w1 + w2 == w and w1%2==0 and w2%2==0:
            success = True
if success:print("YES")
else:print("NO")
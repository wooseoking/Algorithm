a = list(map(int,input().split()))

ascend = sorted(a)
descend = sorted(a,reverse=True)

if a==ascend:
    print("ascending")
elif a == descend:
    print("descending")
else:
    print("mixed")
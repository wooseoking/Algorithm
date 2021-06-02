a = list(map(int,input().split()))
reference = [100,100,200,200,300,300,400,400,500]
if sum(a) < 100:
    print("none")
    exit(0)
for v,ref in zip(a,reference):
    if v > ref:
        print("hacker")
        exit(0)

print("draw")
tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    energy = sum(a)
    if m >= energy:
        print(0)
    else:
        print(abs(m-energy))
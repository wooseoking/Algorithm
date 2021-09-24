testcase = int(input())
for _ in range(testcase):
    a = list(map(int,input().split()))
    a.sort(reverse= True)
    print(a[2])
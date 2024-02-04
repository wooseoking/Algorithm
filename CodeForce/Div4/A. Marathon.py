tc = int(input())
for _ in range(tc):
    a = list(map(int,input().split()))
    me = a[0]
    ans = list(filter(lambda x : x>me,a[1:]))
    print(len(ans))


t = int(input())
def bigger(x,y):
    return x if x>y else y

for _ in range(t):
    a,b,c = map(int,input().split())
    win_for_a = bigger(b,c)
    win_for_b = bigger(a, c)
    win_for_c = bigger(a, b)
    a1,b1,c1 = 0,0,0
    if win_for_a - a>=0:
        a1 = win_for_a-a+1
    if win_for_b - b >= 0:
        b1 =win_for_b-b+1
    if win_for_c - c >= 0:
        c1 = win_for_c-c+1
    print(a1,b1,c1)
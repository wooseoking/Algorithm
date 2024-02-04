tc = int(input())
for _ in range(tc):
    n = int(input())
    x = n//3
    if n % 3 == 0 :
        print(x,x+1,x-1)
    elif n % 3 == 1:
        print(x,x+2,x-1)
    elif n % 3 == 2:
        print(x+1,x+2,x-1)



import itertools
import sys
input = sys.stdin.readline
board = list(list(map(int,input().split())) for _ in range(3))
arr = [v for v in range(1,10)]
U = list(itertools.permutations(arr,len(arr)))

def check_row(a):
    temp1 = sum(a[0])
    temp2 = sum(a[1])
    temp3 = sum(a[2])
    return temp1 == temp2 == temp3 ==15

def check_col(a):
    temp1 = 0
    temp2 = 0
    temp3 = 0

    for i in range(3):temp1 += a[i][0]
    for i in range(3):temp2 += a[i][1]
    for i in range(3):temp3 += a[i][2]
    return temp1 == temp2 == temp3 ==15

def check_dx(a):
    temp1 = 0
    temp2 = 0
    for i in range(3):
        temp1+=a[i][i]
    for i in range(3):
        for j in range(3):
            if i+j+1==3:temp2+=a[i][j]
    return temp1 == temp2 == 15

ans = 1e9

for array in U:
    if sum(array[:3])!=15:continue
    new_a =[[0]*3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            new_a[i][j] = array[i*3+j]

    if check_row(new_a) and check_col(new_a) and check_dx(new_a):
        dif_ =0

        for i in range(3):
            for j in range(3):
                if new_a[i][j] != board[i][j]:
                    dif_+=abs(new_a[i][j]-board[i][j])
        ans = min(dif_,ans)
print(ans)

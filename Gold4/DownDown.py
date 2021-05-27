import sys
input = sys.stdin.readline
n = int(input())
a = [[0]*3 for _ in range(n)]
dp_max = [0]*3
dp_min = [0]*3

for i in range(n):
    e1,e2,e3 = map(int,input().split())
    a[i][0] = e1
    a[i][1] = e2
    a[i][2] = e3
for i in range(3):
    dp_max[i] = a[0][i]
    dp_min[i] = a[0][i]

for i in range(1,n):
    temp_max = dp_max
    arr_max = [0]*3
    arr_max[0] = max(temp_max[0],temp_max[1]) + a[i][0]
    arr_max[1] = max(temp_max[0],temp_max[1],temp_max[2])+a[i][1]
    arr_max[2] = max(temp_max[1], temp_max[2]) + a[i][2]
    temp_max[0] = arr_max[0]
    temp_max[1] =arr_max[1]
    temp_max[2] = arr_max[2]


    temp_min = dp_min
    arr_min = [0] * 3
    arr_min[0] = min(temp_min[0], temp_min[1]) + a[i][0]
    arr_min[1] = min(temp_min[0], temp_min[1], temp_min[2]) + a[i][1]
    arr_min[2] = min(temp_min[1], temp_min[2]) + a[i][2]
    temp_min[0] = arr_min[0]
    temp_min[1] = arr_min[1]
    temp_min[2] = arr_min[2]

max_ans = max(dp_max)
min_ans = min(dp_min)
print(max_ans,min_ans)

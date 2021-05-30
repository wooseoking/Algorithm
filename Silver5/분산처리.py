import sys
input = sys.stdin.readline
n,m = map(int,input().split())
table1 = dict()
table2 = dict()
for i in range(1,n+1):
    pocket = input().strip()
    table1[pocket] = str(i)
    table2[str(i)] = pocket
for _ in range(m):
    what = input().strip()
    if what.isdigit():
        print(table2[what])
    else:
        print(table1[what])

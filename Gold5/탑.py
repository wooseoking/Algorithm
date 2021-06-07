import sys
input = sys.stdin.readline
n = int(input())
temp = list(map(int,input().split()))
a = []
stack1 = []
for i in range(len(temp)):
    stack1.append((temp[i],i+1))
stack2 = []
ans = [0]*n

while stack1:
    v,idx = stack1.pop()

    if not stack2:
        stack2.append((v,idx))
    else:
        while stack2:
            v2,idx2 = stack2[-1]
            if v>v2:
                ans[idx2-1] = idx
                stack2.pop()
            else:break
        stack2.append((v,idx))
for v in ans:
    print(v,end=' ')
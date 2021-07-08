import itertools

t = int(input())
n1 = int(input())
a = list(map(int,input().split()))
n2 = int(input())
b = list(map(int,input().split()))
A ,B =[],[]
for i in range(0,n1):
    for j in range(i,n1):
        A.append(sum(a[i:j+1]))
for i in range(0,n2):
    for j in range(i,n2):
        B.append(sum(b[i:j+1]))
left,right = 0,0
A.sort()
B.sort(reverse=True)
ans = 0
n1,n2 = len(A),len(B)
while left<n1 and right<n2:
    #정답
    if A[left] + B[right] == t:
        c1,c2 = 1,1
        left+=1
        right+=1
        while left<n1 and A[left] == A[left-1]:
            left+=1
            c1+=1
        while right<n2 and B[right] == B[right-1]:
            right+=1
            c2+=1
        ans+=c1*c2
    elif A[left] + B[right] > t:
        right+=1
    else:
        left+=1

print(ans)
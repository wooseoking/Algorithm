n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
result = []

def inside(y,x):
    return 0<=y<n and 0<=x<m

for length in range(0,50):
    for i in range(n):
        for j in range(m):
            if inside(i,j+length) and inside(i+length,j) and inside(i+length,j+length):
                if a[i][j]==a[i][j+length] ==a[i+length][j]== a[i+length][j+length]:
                    result.append((length+1)**2)

print(max(result) if result else 1)
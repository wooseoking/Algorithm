n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
result = []
for i,v in enumerate(arr):
    result.append(arr[i]*(n-i))
print(max(result))
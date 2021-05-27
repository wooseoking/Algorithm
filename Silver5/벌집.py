n = int(input())
if n ==1:
    print(1)
else :
    def get(m):
        return 3*m*m - 3*m+1

    left = 1
    right = 1000000000
    ans = 0
    while left<=right:
        mid = (left+right)//2
        if n <= get(mid):
            ans = mid
            right = mid-1
        else :
            left = mid+1

    print(ans)
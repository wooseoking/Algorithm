def solution(n, times):
    answer = 0
    left = 1
    right = 10000000000000
    while left<=right:
        mid = (left+right)//2
        Sum = 0
        for v in times:
           Sum+=mid//v
        if Sum >=n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer
n =3
times = [1,1,1]
print(solution(n,times))
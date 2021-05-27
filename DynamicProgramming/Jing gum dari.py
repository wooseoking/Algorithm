def solution(stones, k):
    answer = 0
    left =1
    right=max(stones)

    while left <=right:
        mid = (left+right)//2
        zeros =0
        max_zeros = 0
        for ele in stones:
            if ele - mid <0:
                zeros+=1
                if max_zeros <zeros:max_zeros = zeros
            else :zeros = 0
        #가능한 경우
        if max_zeros<k:
            answer = mid
            left = mid+1
        else :right = mid-1
    return answer
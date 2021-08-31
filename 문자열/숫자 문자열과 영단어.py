def solution(s):
    strs = 'zero one two three four five six seven eight nine'
    nums = '0 1 2 3 4 5 6 7 8 9'
    strs = list(strs.split(' '))
    nums = list(nums.split(' '))
    for i in range(10):
        s = s.replace(strs[i],nums[i])
    answer = int(s)
    return answer
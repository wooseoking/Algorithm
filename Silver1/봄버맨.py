# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    a = list(v for v in binary)
    a_idx = []
    for i in range(len(a)):
        if a[i]=='1':a_idx.append(i)
    length = []
    for v1,v2 in zip(a_idx,a_idx[1:]):
        length.append(v2-v1-1)
    if len(length)==0:return 0
    return max(length)
solution(1041)
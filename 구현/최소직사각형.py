
def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]>sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]

    v1,v2 = -1,-1
    for i in range(len(sizes)):
        v1 = max(v1,sizes[i][0])
        v2 = max(v2,sizes[i][1])

    return v1*v2
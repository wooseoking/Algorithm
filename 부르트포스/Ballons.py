import sys
sys.setrecursionlimit(10000000)
Sets = set()

def go(a,select):
    if len(a) == 1:
        Sets.add(a[0])
        return
    #두개 선택해야함

    for i in range(0,len(a)-1):
        idx1 = i
        idx2 = i+1
        if a[idx1]>a[idx2]:
            next_a = [v for v in a if v!=a[idx1]]
            go(next_a,select)
            if not select:
                next__a = [v for v in a if v!=a[idx2]]
                go(next__a,True)

        else :
            next_a = [v for v in a if v != a[idx2]]
            go(next_a, select)
            if not select:
                next__a = [v for v in a if v!= a[idx1]]
                go(next__a, True)

def solution(a):
    answer = 0
    go(a,False)
    print(Sets)
    answer = len(Sets)
    return answer

import sys
sys.setrecursionlimit(200000000)


ans = 0

def solution(n):
    sero = [False]*(n*n)
    Diagnal = [False]*(n*n)
    XDiagnal = [False]*(n*n)

    def go(row,n):
        global ans
        if row == n:
            ans+=1
            return
        for col in range(n):
            if not sero[col] and not Diagnal[row+col] and not XDiagnal[n-row+col-1]:
                sero[col] =True
                Diagnal[row+col]= True
                XDiagnal[n-row+col-1] = True
                go(row+1,n)
                sero[col] = False
                Diagnal[row + col] = False
                XDiagnal[n - row + col-1] = False
        return

    go(0,n)
    return ans

n = int(input())
print(solution(n))
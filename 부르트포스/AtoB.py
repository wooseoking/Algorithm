ans = 1e9
def go(A,B,cnt):
    global ans
    if A==B:
        ans = min(ans,cnt)
        return
    if len(B)==0:return

    last_num = B[-1]
    temp = int(B)
    if temp%2==0: go(A,f"{int(B)//2}",cnt+1)
    if last_num =="1":go(A,B[:len(B)-1],cnt+1)

a,b = input().split()
go(a,b,0)
if ans != 1e9 : print(ans+1)
else : print(-1)
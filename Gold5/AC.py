import sys
input =sys.stdin.readline

def go(string,array):
    Order = True
    left = 0
    right = len(array)-1
    for op in string:
        if op=="R":
            Order = not Order
        elif op=="D":
            if Order:
                left+=1
            else:
                right-=1
    answer = ""
    ret = []
    print(Order,left,right)
    print(type(array))
    if left<=right and Order:
        for v in array[left:right+1]:
            ret.append(str(v)+",")
        ret.pop()
        ret.insert(0,"[")
        ret.insert(-1,"]")
        answer += ''.join(ret)
        print(answer)
    elif left<=right and not Order:
        for v in array[left:right + 1]:
            ret.append(str(v) + ",")
        ret.reverse()
        ret.pop()
        ret.insert(0,"[")
        ret.insert(-1,"]")
        answer += ''.join(ret)
        print(answer)
    else:
        answer += "error"
    return answer

t = int(input())
for _ in range(t):
    query = input().strip()
    n = int(input())
    a = eval(input())
    if n != 0:
        ans = go(query,a)
        print(ans)
    else:
        if "D" in query:print("error")
        else :print("[]")

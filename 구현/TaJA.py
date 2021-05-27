String = input()
small_left = "qwertyasdfgzxcvb"
capital_left = "QWERTYASDFGZXCVB"
small_right = "uiophjklnm"
capital_right = "UIOPHJKLNM"
left = 0
right = 0
other = 0
for char in String:
    if char in small_left:
        left+=1
    elif char in capital_left:
        left+=1
        other+=1
    elif char in small_right:
        right+=1
    elif char in capital_right:
        right+=1
        other+=1
    else:
        other+=1

if right - (other + left) > 1:
    print(left+other,right)
elif left-(other+right)>1:
    print(left,right+other)
else :
    total = left + other + right
    if total%2==0:
        print(total//2,total//2)
    else:
        print(total//2+1,total//2)
import sys
import math
input = sys.stdin.readline
x1,y1,x2,y2,x3,y3 = map(int,input().split())

if (y1-y2)*(x2-x3) == (x1-x2)*(y2-y3):
    print(-1)
else :
    result =[]
    d1 = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
    d2 = math.sqrt(pow(x1-x3,2) + pow(y1-y3,2))
    d3 = math.sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
    result.append(d1)
    result.append(d2)
    result.append(d3)
    result.sort()
    long = 2*(result[1] + result[2])
    short = 2*(result[0] + result[1])
    print(long-short)
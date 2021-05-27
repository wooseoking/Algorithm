import sys
input = sys.stdin.readline

a = []
d = [0 for i in range(8001)]
Sum = 0
n = int(input())

for _ in range(n):
    x = int(input())
    d[x+4000]+=1
    Sum+=x
    a.append(x)

a.sort()
Mean_ = round(Sum/n)
Median_ = a[n//2]
Freq = [i for i,value in enumerate(d) if value == max(d)]
R = a[-1] - a[0]

print(Mean_)
print(Median_)
if len(Freq)==1:
    print(Freq[0]-4000)
else:
    print(Freq[1]-4000)
print(R)

n,k = map(int,input().split())

a = [i for i in range(100000+1)]

prefix_sum = [0]*len(a)
for i in range(1,len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + a[i]

candidate = []
for i in range(len(prefix_sum)-k):
    if prefix_sum[i+k] - prefix_sum[i]<=n:
        candidate.append([j for j in range(i+1,i+k+1)])
if not candidate:
    print(-1)
    exit(0)

ans_list = candidate[-1]
nowsum = sum(ans_list)
diff = abs(nowsum-n)
cnt = 0

for i in range(len(ans_list)-1,-1,-1):
    ans_list[i]+=1
    cnt+=1
    if cnt == diff:break
print(ans_list[-1] - ans_list[0])
n = int(input())
a = list(map(int,input().split()))
largest_length = 0
cnt = 0
for v in a:
    to_binary = bin(v)[2:]
    cnt+=to_binary.count("1")
    largest_length = max(largest_length,len(to_binary))
print(cnt+largest_length-1)
ref,me = map(int,input().split())

for i in range(me):
    source_x = int((ref/me)*i + 0.5)
    print(source_x,end=' ')
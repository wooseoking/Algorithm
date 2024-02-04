tc = int(input())
for _ in range(tc):
    h,m = input().split()
    hour,minute = h.split(':')
    hour = int(hour)
    minute = int(minute)
    m = int(m)
    my_min = hour * 60 + minute
    table = set()
    table.add(my_min)
    while True:
        my_min += m
        while my_min > 1440:
            my_min-=1440

        if my_min in table:break
        table.add(my_min)

    res = set()
    ans = 0
    for e in table:
        c = ''
        res_hour,res_min = str(e // 60) , str(e % 60)
        res_hour = res_hour.zfill(2)
        res_min = res_min.zfill(2)
        tmp = res_hour + res_min
        if tmp == '2400':
            tmp = '0000'
        res.add(tmp)

    for tmp in res:

        if tmp[0] == tmp[-1] and tmp[1] == tmp[2]:
            ans+=1
    print(ans)
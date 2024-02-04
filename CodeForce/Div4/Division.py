t = int(input())
for _ in range(t):
    rating = int(input())
    if 1900 <=rating:
        print('Division 1')
    elif 1600<=rating<1900:
        print('Division 2')
    elif 1400<=rating<1600:
        print('Division 3')
    elif rating <1400:
        print('Division 4')
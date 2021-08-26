query = input()
happy = ':-)'
sad = ':-('
h = query.count(happy)
s = query.count(sad)
if h==0 and s==0:
    print('none')
    exit(0)
if s==h:
    print('unsure')
elif h>s:
    print('happy')
else:
    print('sad')